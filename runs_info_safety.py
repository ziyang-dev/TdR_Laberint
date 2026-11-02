from data_manager import load_run_id, divide_by_category, load_determined_run_info
from chart_manager import int_or_float
from config import runs_path, error_info_runs_path, connection
from data_collector import collect_data
import random

#Critical Values for Dixon's Q-Test alpha=0.05:
critical_values={3:0.970,4:0.829,5:0.710}

def change_dict_is_outlier(run_id, info, info_type=None, run_id_list=None):
    if info=="?":
        if info_type==None or run_id_list==None:
            raise Exception ("Need 5 parameter insted of 3 in change_dict_is_outlier when info=='?'")
        print_error_info(run_id, info_type, run_id_list)
    connection.execute(
        "UPDATE runs SET is_outlier = ? WHERE run_id = ?",
        (info, run_id))
    connection.commit()


def print_error_info(run_id, info_type, run_id_list):
    with open(error_info_runs_path, "a", encoding="utf-8", newline="") as file:
        file.write(f"{run_id}  ---  Info type: {info_type}   ---   {run_id_list} \n")

def verify_runs_safety(*, auto_generate_maze=False):
    have_info_error=False
    while True:
        undefined_run_id_list=load_run_id(is_outlier="U")
        dict_by_maze=divide_by_category(undefined_run_id_list,"maze_id","run_id")
        for key, values in dict_by_maze.items():
            dict_by_maze[key]=divide_by_category(values,"solver_algorithm", "run_id")

        need_generate_maze_list=[]
        for maze_id, dict_by_solver in dict_by_maze.items():
            for solver_algorithm, run_id_list in dict_by_solver.items():
                run_id_pop_list=[]
                while len(run_id_list)>5:
                    run_id_pop_list.append(run_id_list.pop())
                will_break=False
                while run_id_list!="Finish":
                    while len(run_id_list)<5:
                        if run_id_pop_list:
                            run_id_list.append(run_id_pop_list.pop())
                            continue
                        will_break=True
                        break
                    if will_break:
                        break
                    for info_type in ["execution_time", "memory_peak"]:
                        list_for_dixon = sorted((load_determined_run_info(run_id, info_type), run_id) for run_id in run_id_list)
                        try:
                            Q1=(list_for_dixon[1][0]-list_for_dixon[0][0])/ (list_for_dixon[4][0]-list_for_dixon[0][0])
                        except ZeroDivisionError:
                            Q1=0
                        if Q1 > critical_values[5]:
                            error_run_id = list_for_dixon[0][1]
                            run_id_list=[]
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q1/{Q1}/!!!!!!!!!!!!!!!!!!", list_for_dixon)
                            for i in range(1,5):
                                change_dict_is_outlier(list_for_dixon[i][1],"!")
                            break
                        try:
                            Q3=(list_for_dixon[2][0]-list_for_dixon[1][0])/(list_for_dixon[2][0]-list_for_dixon[0][0])
                        except ZeroDivisionError:
                            Q3=0
                        try:
                            Q4=(list_for_dixon[3][0]-list_for_dixon[2][0])/(list_for_dixon[3][0]-list_for_dixon[0][0])
                        except ZeroDivisionError:
                            Q4=0
                        try:
                            Q5=(list_for_dixon[4][0]-list_for_dixon[3][0])/(list_for_dixon[4][0]-list_for_dixon[0][0])
                        except ZeroDivisionError:
                            Q5=0
                        if Q3 > critical_values[3]:
                            error_run_id = list_for_dixon[2][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q3/{Q3}", list_for_dixon)
                            error_run_id = list_for_dixon[3][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q3-4/{Q4}", list_for_dixon)
                            error_run_id = list_for_dixon[4][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q3-5/{Q5}", list_for_dixon)
                            break
                        if Q4 > critical_values[4]:
                            error_run_id = list_for_dixon[3][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q4/{Q4}", list_for_dixon)
                            error_run_id = list_for_dixon[4][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q4-5/{Q5}", list_for_dixon)
                            break
                        if Q5 > critical_values[5]:
                            error_run_id = list_for_dixon[4][1]
                            run_id_list.remove(error_run_id)
                            change_dict_is_outlier(error_run_id,"?",f"{info_type}/Q5/{Q5}", list_for_dixon)
                            break
                    else:
                        for info_type in ["vertices_explored","movement_steps"]:
                            info=load_determined_run_info(run_id_list[0], info_type)
                            for run_id in run_id_list:
                                if info!=load_determined_run_info(run_id, info_type):
                                    error_run_id=run_id
                                    run_id_list.remove(error_run_id)
                                    change_dict_is_outlier(error_run_id,"?",f"{info_type}/{info}", run_id_list)
                                    have_info_error=True
                                    break
                        else:
                            for run_id in run_id_list:
                                change_dict_is_outlier(run_id,"S")
                            run_id_list="Finish"
                else:
                    for run_id in run_id_pop_list:
                        change_dict_is_outlier(run_id,"E")
                    continue
                need_generate_maze_list.append([maze_id,solver_algorithm,5-len(run_id_list)])
        if have_info_error:
            raise Exception("have not the same path_len not explore_node")
        if auto_generate_maze:
            if need_generate_maze_list!=[]:
                generation_tasks = []
                for maze_id, solver_algorithm, count in need_generate_maze_list:
                    for _ in range(count):
                        generation_tasks.append((maze_id, solver_algorithm))
                random.shuffle(generation_tasks)
                for maze_id, solver_algorithm in generation_tasks:
                    collect_data(maze_id, solver_algorithm)
                yield
            else:   
                return
        else:
            return


def delete_Uinfo():
    undefined_run_id_list=load_run_id(is_outlier="U")
    if undefined_run_id_list==[]:
        return "Not detected undefined info"
    generation_tasks = []
    for run_id in undefined_run_id_list:
        change_dict_is_outlier(run_id,"O",f"out of limit", "-")
        maze_id, solver_algorithm=load_determined_run_info(run_id, "maze_id", "solver_algorithm")
        generation_tasks.append((maze_id, solver_algorithm))
    random.shuffle(generation_tasks)
    for maze_id, solver_algorithm in generation_tasks:
        collect_data(maze_id, solver_algorithm)
    return f"Detected {len(undefined_run_id_list)} undefined info"