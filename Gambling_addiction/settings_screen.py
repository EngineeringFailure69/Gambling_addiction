import pygame
import const
import sys
import utils.utils as utils
import utils.draw_functions as draw_functions
import os

def settings_screen():
    running = True

    back_icon_path = "icons\\go_back_icon.png"
    back_icon_position_x = 0
    back_icon_position_y = 0
    back_icon_width = 150
    back_icon_height = 70

    apply_button_height = 50
    apply_button_width = 200
    apply_button_position_x = const.screen.get_width() / 2 - apply_button_width / 2
    apply_button_position_y = const.screen.get_height()-100

    fps_text_width = 200
    fps_text_position_x = const.screen.get_width() / 2 - fps_text_width
    fps_text_position_y = const.screen.get_height() - 550
    fps_text_height = 30

    show_fps_button_height = 30
    show_fps_button_position_x = fps_text_position_x + fps_text_width
    show_fps_button_position_y = fps_text_position_y - show_fps_button_height / 6
    show_fps_button_width = 150
    show_fps_button_text = ""

    open_file_dialog_button_height = 30
    open_file_dialog_button_width = 200
    open_file_dialog_button_position_x = const.screen.get_width() / 2 - 1.5 * open_file_dialog_button_width
    open_file_dialog_button_position_y = 150
    
    show_fps_button_rect = pygame.Rect(show_fps_button_position_x, show_fps_button_position_y, show_fps_button_width, show_fps_button_height)
    apply_button_rect = pygame.Rect(apply_button_position_x, apply_button_position_y, apply_button_width, apply_button_height)
    fps_text_rect = pygame.Rect(fps_text_position_x, fps_text_position_y, fps_text_width, fps_text_height)
    open_file_dialog_button_rect = pygame.Rect(open_file_dialog_button_position_x, open_file_dialog_button_position_y, open_file_dialog_button_width, open_file_dialog_button_height)
    font = pygame.font.SysFont(None, 30)

    if const.fps_show:
        show_fps_button_text = "Yes"
    else:
        show_fps_button_text = "No"

    new_playlist = None
    while running:
        const.screen.fill(const.green)
        events = pygame.event.get()

        mouse_pos = pygame.mouse.get_pos()

        draw_functions.draw_button(const.screen, const.blue, show_fps_button_rect, show_fps_button_text, font, const.black, mouse_pos)
        back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height = draw_functions.load_icons(const.screen, back_icon_path, back_icon_width, back_icon_height, back_icon_position_x, back_icon_position_y)
        back_icon_rect = pygame.Rect(back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height)
        draw_functions.draw_button(const.screen, const.blue, apply_button_rect, "Apply", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, open_file_dialog_button_rect, "Load new playlist", font, const.black, mouse_pos)
        draw_functions.draw_text(const.screen, "Show FPS counter:", const.black, fps_text_rect, font, line_spacing = 5)
        song_path = const.playlist[const.current_song_index]
        song_name = os.path.basename(song_path)
        draw_functions.draw_centered_text_with_other_element_as_reference_point(const.screen, song_name, font, const.black, open_file_dialog_button_rect, x_offset=20)

        utils.play_music()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if show_fps_button_rect.collidepoint(mouse_pos):
                    if const.fps_apply == False:
                        show_fps_button_text = "Yes"
                        const.fps_apply = True
                    elif const.fps_apply == True:
                        show_fps_button_text = "No"
                        const.fps_apply = False
                if  back_icon_rect.collidepoint(mouse_pos):
                    running = False
                    return
                if apply_button_rect.collidepoint(mouse_pos):
                    const.fps_show = const.fps_apply 
                    if new_playlist:
                        pygame.mixer.music.stop()
                        const.playlist = new_playlist
                        const.current_song_index = 0
                        utils.play_current_song()
                if open_file_dialog_button_rect.collidepoint(mouse_pos):
                    custom_playlist, songs = utils.load_playlist()

                    if custom_playlist:
                        new_playlist = list(songs)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)