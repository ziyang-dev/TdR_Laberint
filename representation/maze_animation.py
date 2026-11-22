import pygame
import config
from representation.maze_representation import drawGrid, drawAuxiliaryLines, add_list_to_maze, draw_exit
from data_manager import load_maze

def animate_maze_generation(gen, n):
    maze=next(gen)
    finised=False
    def animate_next():
        nonlocal maze, finised
        try:
            maze=next(gen)
        except StopIteration:
            finised=True
    #calculs d'altres constants
    gridNumber=len(maze)
    gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
    config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores


    #Pygame init
    pygame.init()
    screen = pygame.display.set_mode((config.windows_size,config.windows_size))
    pygame.display.set_caption(config.windowsCaptionText)
    running = True
    clock = pygame.time.Clock()
    flag=1
    while running:
        #Teclats per sortir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                #if event.key == pygame.K_SPACE: #sicronizar animacion
                else:
                    if config.animation_type=="click":
                        animate_next()

        if config.animation_type=="auto":
            animate_next()
        
        screen.fill(config.Color.background) #posar color de fons

        drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
        draw_exit(screen, gridSize, gridNumber)

        if config.with_auxiliary_line:
            drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

        pygame.display.update() #actualitzar per cada frame
        clock.tick(config.ticks) #ajustar a 30 FPS
        if config.save_maze_image and not finised:
            pygame.image.save(screen, f"image/i{n}-{flag:05d}.png")
            flag+=1
    pygame.quit()
    return

def draw_debug_panel(screen, debug_info, panel_x,
                     panel_width, window_height):

    # Colors
    background_color = config.Color.background
    text_color = config.Color.wall
    separator_color = config.Color.gray

    # Fonts
    title_font = pygame.font.SysFont("Arial", 24, bold=True)
    font = pygame.font.SysFont("Arial", 18)

    # Panel background
    pygame.draw.rect(
        screen,
        background_color,
        (panel_x, 0, panel_width, window_height)
    )

    # Layout constants
    margin = 15
    title_height = 50
    line_spacing = 22
    item_spacing = 15

    min_column_width = 100
    max_list_columns = 6

    # Title
    title = title_font.render(
        "INFORMACIÓ", True, text_color
    )

    screen.blit(title, (panel_x + margin, margin))

    content_y = margin + title_height
    available_height = window_height - content_y - margin
    available_width = panel_width - margin * 2

    # -------------------------------------------------
    # 1. Prepare information blocks
    # -------------------------------------------------

    blocks = []

    for name, value in debug_info:

        if isinstance(value, list):
            value = [str(item) for item in value]

            blocks.append({
                "name": name,
                "value": value,
                "is_list": True
            })

        else:
            blocks.append({
                "name": name,
                "value": str(value),
                "is_list": False
            })

    # -------------------------------------------------
    # 2. Calculate layout for each possible column count
    # -------------------------------------------------

    selected_columns = 1
    selected_layout = None

    max_columns = max(
        1,
        available_width // min_column_width
    )

    for column_count in range(1, max_columns + 1):

        column_width = available_width // column_count

        # Calculate block heights
        block_heights = []

        for block in blocks:

            if block["is_list"]:

                # Number of columns used by the list
                list_columns = min(
                    max_list_columns,
                    max(1, column_width // 100)
                )

                rows = (
                    len(block["value"]) + list_columns - 1
                ) // list_columns

                height = (
                    line_spacing * (rows + 1)
                    + item_spacing
                )

            else:

                name_width = font.size(
                    block["name"] + ": "
                )[0]

                value_width = font.size(
                    block["value"]
                )[0]

                if name_width + value_width < column_width - 20:
                    height = line_spacing + item_spacing
                else:
                    height = (
                        line_spacing * 2 + item_spacing
                    )

            block_heights.append(height)

        # Distribute blocks between columns
        column_heights = [0] * column_count
        column_blocks = [[] for _ in range(column_count)]

        for index, block in enumerate(blocks):

            target_column = column_heights.index(
                min(column_heights)
            )

            column_blocks[target_column].append(index)

            column_heights[target_column] += (
                block_heights[index]
            )

        # Check whether everything fits
        if max(column_heights, default=0) <= available_height:

            selected_columns = column_count
            selected_layout = column_blocks
            break

    # If nothing fits completely, use the maximum number of columns
    if selected_layout is None:

        selected_columns = max_columns

        column_heights = [0] * selected_columns
        selected_layout = [[] for _ in range(selected_columns)]

        for index, height in enumerate(block_heights):

            target_column = column_heights.index(
                min(column_heights)
            )

            selected_layout[target_column].append(index)
            column_heights[target_column] += height

    # -------------------------------------------------
    # 3. Draw information
    # -------------------------------------------------

    column_width = available_width // selected_columns

    for column_index, block_indices in enumerate(selected_layout):

        x = (
            panel_x + margin
            + column_index * column_width
        )

        y = content_y

        for block_index in block_indices:

            block = blocks[block_index]

            name = block["name"]
            value = block["value"]

            # -----------------------------
            # Scalar information
            # -----------------------------

            if not block["is_list"]:

                name_text = font.render(
                    name + ":",
                    True,
                    text_color
                )

                value_text = font.render(
                    value,
                    True,
                    text_color
                )

                name_width = name_text.get_width()

                if (
                    name_width + value_text.get_width()
                    < column_width - 20
                ):

                    screen.blit(name_text, (x, y))

                    screen.blit(
                        value_text,
                        (x + name_width + 8, y)
                    )

                    y += line_spacing

                else:

                    screen.blit(name_text, (x, y))
                    y += line_spacing

                    screen.blit(
                        value_text,
                        (x + 10, y)
                    )

                    y += line_spacing

            # -----------------------------
            # List information
            # -----------------------------

            else:

                title_text = font.render(
                    name + ":",
                    True,
                    text_color
                )

                screen.blit(title_text, (x, y))

                y += line_spacing

                list_columns = min(
                    max_list_columns,
                    max(1, column_width // 100)
                )

                cell_width = column_width // list_columns

                for index, item in enumerate(value):

                    row = index // list_columns
                    col = index % list_columns

                    # Automatically reduce font size if the item is too wide
                    item_font_size = 18
                    min_font_size = 9

                    item_string = str(item)

                    while item_font_size > min_font_size:

                        item_font = pygame.font.SysFont(
                            "Arial",
                            item_font_size
                        )

                        if item_font.size(item_string)[0] <= cell_width - 5:
                            break

                        item_font_size -= 1

                    item_text = item_font.render(
                        item_string,
                        True,
                        text_color
                    )

                    item_x = x + col * cell_width
                    item_y = y + row * line_spacing

                    # Clip text to its own column
                    old_clip = screen.get_clip()

                    screen.set_clip(
                        pygame.Rect(
                            item_x,
                            item_y,
                            cell_width,
                            line_spacing
                        )
                    )

                    screen.blit(
                        item_text,
                        (item_x, item_y)
                    )

                    screen.set_clip(old_clip)

                rows = (
                    len(value) + list_columns - 1
                ) // list_columns

                y += rows * line_spacing

            # Separator
            pygame.draw.line(
                screen,
                separator_color,
                (x, y + 5),
                (x + column_width - 10, y + 5),
                1
            )

            y += item_spacing

def draw_debug_panel2(screen, info, panel_x, panel_width, window_height):
    # Fonts
    title_font = pygame.font.SysFont("Arial", 26, bold=True)
    font = pygame.font.SysFont("Arial", 20)

    # Background
    panel_rect = pygame.Rect(
        panel_x, 0, panel_width, window_height
    )
    pygame.draw.rect(screen, (35, 35, 35), panel_rect)

    # Unpack information
    position, stack, explored_cell, status = info

    # Title
    title = title_font.render(
        "INFORMACIÓ DFS", True, (255, 255, 255)
    )
    screen.blit(title, (panel_x + 20, 20))

    # Current position
    if position == "---":
        position_text = "---"
    else:
        position_text = str(position)

    text = font.render(
        f"Posició actual: {position_text}",
        True, (255, 255, 255)
    )
    screen.blit(text, (panel_x + 20, 75))

    # Explored nodes
    text = font.render(
        f"Nodes explorats: {explored_cell}",
        True, (255, 255, 255)
    )
    screen.blit(text, (panel_x + 20, 120))

    # Status
    text = font.render(
        f"Estat: {status}",
        True, (255, 255, 255)
    )
    screen.blit(text, (panel_x + 20, 165))

    # Stack title
    text = font.render(
        "Pila:",
        True, (255, 255, 255)
    )
    screen.blit(text, (panel_x + 20, 220))

    # Show only the last 10 elements
    if len(stack) > 10:
        visible_stack = ["..."] + stack[-10:]
    else:
        visible_stack = stack

    # Draw stack
    y = 260

    for item in visible_stack:
        text = font.render(
            str(item),
            True, (200, 200, 200)
        )
        screen.blit(text, (panel_x + 30, y))
        y += 27

def animate_maze_research(gen, n):
    maze, debug_info=next(gen)
    finised=False
    def animate_next():
        nonlocal maze, debug_info, finised
        try:
            maze, debug_info =next(gen)
        except StopIteration:
            finised=True
    #calculs d'altres constants
    gridNumber=len(maze)
    gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
    config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores

    #Pygame init
    pygame.init()
    if config.with_debug_panel:
        panel_width = config.debug_label_panel_width
        window_height = config.windows_size
        window_width = config.windows_size + panel_width
        screen = pygame.display.set_mode((window_width, window_height))
    else:
        screen = pygame.display.set_mode((config.windows_size, config.windows_size))
    pygame.display.set_caption(config.windowsCaptionText)
    running = True
    clock = pygame.time.Clock()
    flag=1
    while running:
        #Teclats per sortir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                #if event.key == pygame.K_SPACE: #sicronizar animacion
                else:
                    if config.animation_type=="click":
                        animate_next()

        if config.animation_type=="auto":
            animate_next()
        
        screen.fill(config.Color.background) #posar color de fons

        drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
        draw_exit(screen, gridSize, gridNumber)

        if config.with_auxiliary_line:
            drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

        if config.with_debug_panel:
            draw_debug_panel(
                screen,
                debug_info,
                config.windows_size,
                panel_width,
                window_height
            )
        pygame.display.update() #actualitzar per cada frame
        clock.tick(config.ticks) #ajustar a 30 FPS
        if config.save_maze_image and not finised:
            pygame.image.save(screen, f"image/i{n}-{flag:05d}.png")
            flag+=1
    pygame.quit()
    return



def maze_representation(maze_id):
    maze, _ = load_maze(maze_id)

    #calculs d'altres constants
    gridNumber=len(maze)
    gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
    config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores


    #Pygame init
    pygame.init()
    screen = pygame.display.set_mode((config.windows_size,config.windows_size))
    pygame.display.set_caption(config.windowsCaptionText)
    running = True
    clock = pygame.time.Clock()

    while running:
        #Teclats per sortir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False

        
        screen.fill(config.Color.background) #posar color de fons

        drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
        draw_exit(screen, gridSize, gridNumber)

        if config.with_auxiliary_line:
            drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

        pygame.display.update() #actualitzar per cada frame
        clock.tick(config.ticks) #ajustar a 30 FPS
    pygame.quit()
    return

