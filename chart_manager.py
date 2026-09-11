import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import config
from statsmodels.nonparametric.smoothers_lowess import lowess
from data_manager import load_determined_run_info, load_maze

def int_or_float(valor):
    try:
        return int(valor)
    except ValueError:
        return float(valor)

def divide_by_category(run_id_list,category,*info_types):
    maze_dict={}
    if category=="maze_category":
        for run_id in run_id_list:
            category_info, *info=load_determined_run_info(run_id,"maze_id",*info_types)
            if isinstance(info,list):
                result=[int_or_float(n) for n in info]
            else:
                result=int_or_float(info)
            category_info=config.maze_category[category_info[1]][1]
            maze_dict.setdefault(category_info, []).append(result)
    else:
        for run_id in run_id_list:
            category_info, *info=load_determined_run_info(run_id,category,*info_types)
            if len(info)==1:
                info=info[0]
            if isinstance(info,list):
                result=[int_or_float(n) for n in info]
            else:
                result=int_or_float(info)
            maze_dict.setdefault(category_info, []).append(result)
    return maze_dict

def mean_dict_inplace(data_dict):  #dict_type={"key":[folat_list]}
    for key,values in data_dict.items():
        if isinstance(values[0], list):
            data_dict[key] = np.mean(values, axis=0).tolist()
        else:
            data_dict[key] = np.mean(values)

def draw_grid(ax):
    ax.grid(axis='both', linestyle='-.', alpha=0.3)


def chart_1gen1sol1size1info_runs(runs_id_list, info_type,  *, title="Chart type: 1gen1sol1size1info_runs"):
    r_info=[]
    for run_id in runs_id_list:
        r_info.append(float(load_determined_run_info(run_id,info_type)))

    x = np.arange(len(runs_id_list))
    fig, ax = plt.subplots()


    ax.set_xlabel(f"Vegades d'execució: {len(runs_id_list)} vegada/es")
    ax.set_ylabel(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels("", rotation=45, ha="right")
    ax.set_ylim(bottom=0, top=max(r_info)*1.1)

    mean_value=np.mean(r_info)
    ax.axhline(y=mean_value,color="r", linestyle="--", linewidth=1.5, label=f"Mitjana: {mean_value:.5f} {config.runs_unit_label[info_type]}")

    ax.plot(x,r_info)
    
    draw_grid(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()

def chart_1gen1sol1size1info_maze(runs_id_list, info_type,  *, title="Chart type: 1gen1sol1size1info_maze"):
    maze_dict=divide_by_category(runs_id_list,"maze_id",info_type)
    mean_dict_inplace(maze_dict)

    m_info=list(maze_dict.values())

    x = np.arange(len(maze_dict))

    fig, ax = plt.subplots()


    ax.set_xlabel(f"Nombre de laberints: {len(maze_dict)} laberint/s ({len(runs_id_list)} runs)")
    ax.set_ylabel(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels("", rotation=45, ha="right")
    ax.set_ylim(bottom=0, top=max(m_info)*1.1)

    mean_value=np.mean(m_info)
    ax.axhline(y=mean_value,color="r", linestyle="--", linewidth=1.5, label=f"Mitjana: {mean_value:.5f} {config.runs_unit_label[info_type]}")

    ax.plot(x,m_info)

    draw_grid(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()

def chart_1gen3sol1size1info_maze(runs_id_list, info_type,  *, title="Chart type: 1gen3sol1size1info_maze"):
    maze_dict=divide_by_category(runs_id_list,"solver_algorithm","run_id")
    for key,valor in maze_dict.items():
        maze_dict[key]=divide_by_category(valor,"maze_id",info_type)
        mean_dict_inplace(maze_dict[key])


    DFS_info=list(maze_dict["DFS"].values())
    BFS_info=list(maze_dict["BFS"].values())
    A_star_info=list(maze_dict["A_star"].values())

    x = np.arange(len(DFS_info))

    fig, ax = plt.subplots()


    ax.set_xlabel(f"Nombre de laberints: {len(DFS_info)} laberint/s ({len(runs_id_list)} runs)")
    ax.set_ylabel(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels("", rotation=45, ha="right")
    ax.set_ylim(bottom=0, top=max(max(DFS_info),max(BFS_info),max(A_star_info))*1.1)
    mean_DFS=np.mean(DFS_info)
    mean_BFS=np.mean(BFS_info)
    mean_A_star=np.mean(A_star_info)
    ax.axhline(y=mean_DFS,color="C0", linestyle="--", linewidth=1.5, label=f"Mitjana: {mean_DFS:.5f} {config.runs_unit_label[info_type]}")
    ax.axhline(y=mean_BFS,color="C1", linestyle="--", linewidth=1.5, label=f"Mitjana: {mean_BFS:.5f} {config.runs_unit_label[info_type]}")
    ax.axhline(y=mean_A_star,color="C2", linestyle="--", linewidth=1.5, label=f"Mitjana: {mean_A_star:.5f} {config.runs_unit_label[info_type]}")

    ax.plot(x,DFS_info,color="C0",label="DFS")
    ax.plot(x,BFS_info,color="C1",label="BFS")
    ax.plot(x,A_star_info,color="C2",label="A_star")

    draw_grid(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()

def chart_1gen3sol1size1info_box(runs_id_list, info_type,  *, title="Chart type: 1gen3sol1size1info_box"):
    maze_dict=divide_by_category(runs_id_list,"solver_algorithm","run_id")
    for key,valor in maze_dict.items():
        maze_dict[key]=divide_by_category(valor,"maze_id",info_type)
        mean_dict_inplace(maze_dict[key])


    DFS_info=list(maze_dict["DFS"].values())
    BFS_info=list(maze_dict["BFS"].values())
    A_star_info=list(maze_dict["A_star"].values())

    x = np.arange(len(maze_dict))

    fig, ax = plt.subplots()


    ax.set_xlabel(f"Algorismes de cerca ({len(runs_id_list)} runs)")
    ax.set_ylabel(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    ax.set_title(title)
    ax.set_ylim(bottom=0, top=max(max(DFS_info),max(BFS_info),max(A_star_info))*1.1)

    ax.boxplot(DFS_info, vert=True, patch_artist=True, positions=[0],
            boxprops=dict(facecolor=mcolors.to_rgba('C0', alpha=0.25), color='C0'),
            medianprops=dict(color='r', linewidth=2))
    ax.boxplot(BFS_info, vert=True, patch_artist=True, positions=[1],
            boxprops=dict(facecolor=mcolors.to_rgba('C1', alpha=0.25), color='C1'),
            medianprops=dict(color='r', linewidth=2))
    ax.boxplot(A_star_info, vert=True, patch_artist=True, positions=[2],
            boxprops=dict(facecolor=mcolors.to_rgba('C2', alpha=0.25), color='C2'),
            medianprops=dict(color='r', linewidth=2))

    ax.set_xticks(x)
    ax.set_xticklabels(["DFS","BFS","A_star"], rotation=45, ha="right")

    draw_grid(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()

def chart_9gen3sol1size1info_heap(runs_id_list, info_type,  *, title="Chart type: chart_9gen3sol1size1info_heap"):
    maze_dict=divide_by_category(runs_id_list,"solver_algorithm","run_id")
    for key,valor in maze_dict.items():
        maze_dict[key]=divide_by_category(valor,"maze_category",info_type)
        mean_dict_inplace(maze_dict[key])

    def order_gen_in_list(dict):
        result_list=[None for _ in range(len(dict))]
        for i in range(len(dict)):
            category=config.maze_category[str(i+1)][1]
            result_list[i]=dict[category]
        return result_list


    info_list=[order_gen_in_list(maze_dict["DFS"]),order_gen_in_list(maze_dict["BFS"]),order_gen_in_list(maze_dict["A_star"])]
    n=len(info_list[0])
    for i in range(1,len(info_list)):
        if n!=len(info_list[i]):
            raise Exception ("There is not the same category runs for all solver, chart_9gen3sol1size1info_heap")

    fig, ax = plt.subplots()


    ax.set_xlabel(f"Algorismes de generació de laberints ({len(runs_id_list)} runs)")
    ax.set_ylabel("Algorismes de cerca")
    ax.set_title(title)

    heatmap = ax.imshow(info_list, cmap="plasma", aspect="auto")
        
    x_ticks_label=list(maze_dict["DFS"].keys())
    for i in range(len(x_ticks_label)):
        x_ticks_label[i]=config.generator_algorithm_label[x_ticks_label[i]]
    ax.set_xticks(range(len(info_list[0])))
    ax.set_xticklabels(x_ticks_label,  rotation=45, ha="right")
    ax.set_yticks(range(len(info_list)))
    ax.set_yticklabels(["DFS", "BFS", "A_star"])

    threshold=(max(max(row) for row in info_list)+min(min(row) for row in info_list))/2
    
    for i in range(len(info_list)):
        for j in range(len(info_list[0])):
            val = info_list[i][j]
            text_label = f"{val:.3g}" 
            text_color = "w" if info_list[i][j] < threshold else "k"
            ax.text(
                j, i,
                text_label,
                ha="center",
                va="center",
                color=text_color
                )

    fig.colorbar(heatmap, ax=ax).set_label(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    plt.tight_layout()
    plt.show()

def chart_9gen1sol1size1info_bar(runs_id_list, info_type,  *, title="Chart type: chart_9gen1sol1size1info_bar"):

    maze_dict=divide_by_category(runs_id_list,"maze_category",info_type)
    mean_dict_inplace(maze_dict)

    def order_gen_in_list(dict):
        result_list=[None for _ in range(len(dict))]
        for i in range(len(dict)):
            category=config.maze_category[str(i+1)][1]
            result_list[i]=dict[category]
        return result_list


    info_list=order_gen_in_list(maze_dict)
  
    fig, ax = plt.subplots()


    ax.set_xlabel(f"Algorismes de generació de laberints ({len(runs_id_list)} runs)")
    ax.set_ylabel(f"{config.runs_label[info_type]} ({config.runs_unit_label[info_type]})")
    ax.set_title(title)

    x = np.arange(len(info_list))
    x_ticks_label=list(maze_dict.keys())

    ax.bar(x, info_list)

    for i in range(len(x_ticks_label)):
        x_ticks_label[i]=config.generator_algorithm_label[x_ticks_label[i]]
    
    ax.set_xticks(x)
    ax.set_xticklabels(x_ticks_label,  rotation=45, ha="right")

    draw_grid(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()

def chart_1gen1sol1size1info_optim_pie(runs_id_list,  *, title="Chart type: chart_1gen1sol1size1info_optim_pie"):
    maze_dict={}

    mean_list=[0,0]

    for run_id in runs_id_list:
        is_optimal,path_len,maze_id=load_determined_run_info(run_id,"is_optimal","path_length","maze_id")
        if int(is_optimal):
            maze_dict[-1]=maze_dict.setdefault(-1, 0) + 1
        else:
            path_len=int(path_len)
            _, optimal_path_len=load_maze(maze_id)
            mean_list[0] += (path_len/optimal_path_len-1)*100
            mean_list[1] += 1
            percert=int((path_len/optimal_path_len-1)*10)*10
            maze_dict[percert]=maze_dict.setdefault(percert, 0) + 1

    items = sorted(maze_dict.items())
    keys = [key for key, _ in items]
    values = [value for _, value in items]

    labels=[]
    for key in keys:
        if key==-1:
            result="Òptim"
        else:
            result=f"{key}%-{key+10}% més"
        labels.append(result)

    explode= [0 for _ in keys]
    if keys[0]==-1:
        explode[0]=0.05
  
    fig, ax = plt.subplots()

    ax.set_title(title)
    
    ax.pie(
        values, 
        explode=explode, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90
    )

    if -1 in maze_dict:
        info_text = f"{(1-maze_dict[-1]/len(runs_id_list))*100}% de camins no òptims"
    else:
        info_text = f"100% de camins no òptims"
    if mean_list[1]!=0:
        mean=int(mean_list[0]/mean_list[1]*100)/100
    else:
        mean="---"
    info_text+=f"\namb una mitjana de {mean}% més \nde caselles ({len(runs_id_list)} runs)"
    empty_square = ax.plot([], [], label=info_text, color='none')[0]
    ax.legend(
        handles=[empty_square], 
        loc='best',
        frameon=True,
        facecolor='white',
        edgecolor='#CCCCCC',
        fontsize=9
    )

    plt.tight_layout() 
    plt.show()

def chart_1gen1sol1size2info_ver_time(runs_id_list,  *, title="Chart type: chart_1gen1sol1size2info_ver_time"):
    maze_dict=divide_by_category(runs_id_list,"maze_id","vertices_explored","execution_time")
    mean_dict_inplace(maze_dict)

    vertices_explored_list=[]
    execution_time_list=[]
    for value in maze_dict.values():
        vertices_explored_list.append(value[0])
        execution_time_list.append(value[1])

    fig, ax = plt.subplots()


    ax.set_xlabel(f"Caselles explorades (casella/es) ({len(runs_id_list)} runs)")
    ax.set_ylabel(f"Temps d'execució (ms)")
    ax.set_title(title)
    ax.set_ylim(bottom=0, top=max(execution_time_list)*1.1)

    result = lowess(execution_time_list, vertices_explored_list, frac=0.6)

    x_smooth = result[:, 0]
    y_smooth = result[:, 1]

    ax.scatter(vertices_explored_list, execution_time_list)
    ax.plot(x_smooth, y_smooth)

    draw_grid(ax)
    plt.tight_layout()
    plt.show()

'''
ril=[]
for i in range (448,450+1):
    if load_determined_run_info(i,"solver_algorithm") !="DFS":
        continue
    ril.append(i)
chart_1gen1sol1size1info_runs(ril,"execution_time")'''
#run_id,experiment_id,maze_id,solver_algorithm,is_solved,execution_time,vertices_explored,path_length,is_optimal,memory_peak'''