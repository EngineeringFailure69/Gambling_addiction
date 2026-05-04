import pygame
import const
import sys
import utils.utils as utils
import utils.draw_functions as draw_functions
import os
import text_messages 

def settings_screen():
    running = True

    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()

    back_icon_path = "icons\\go_back_icon.png"
    back_icon_position_x = 0
    back_icon_position_y = 0
    back_icon_width = 150
    back_icon_height = 70

    apply_button_height = 50
    apply_button_width = 200
    apply_button_position_x = screen_width / 2 - apply_button_width / 2
    apply_button_position_y = screen_height - 100

    fps_text_width = 200
    fps_text_position_x = screen_width / 2 - fps_text_width
    fps_text_position_y = screen_height / 12
    fps_text_height = 30

    show_fps_button_height = 30
    show_fps_button_position_x = fps_text_position_x + fps_text_width
    show_fps_button_position_y = fps_text_position_y - show_fps_button_height / 6
    show_fps_button_width = 150
    show_fps_button_text = ""

    open_file_dialog_button_height = 30
    open_file_dialog_button_width = 200
    open_file_dialog_button_position_x = screen_width / 2 - 1.5 * open_file_dialog_button_width
    open_file_dialog_button_position_y = screen_height / 5

    volume_button_height = 30
    volume_button_width = 200
    volume_button_position_x = screen_width / 2 - volume_button_width / 2 - 10
    volume_button_position_y = screen_height / 3

    increase_volume_button_height = 30
    increase_volume_button_width = 50
    increase_volume_button_position_x = volume_button_position_x + volume_button_width + 20
    increase_volume_button_position_y = volume_button_position_y

    decrease_volume_button_height = 30
    decrease_volume_button_width = 50
    decrease_volume_button_position_x = volume_button_position_x - decrease_volume_button_width - 20
    decrease_volume_button_position_y = volume_button_position_y

    directory_playlist_button_width = 200
    directory_playlist_button_height = 30
    directory_playlist_button_position_x = screen_width / 2 - directory_playlist_button_width / 2
    directory_playlist_button_position_y = screen_height / 2

    show_fps_button_rect = pygame.Rect(show_fps_button_position_x, show_fps_button_position_y, show_fps_button_width, show_fps_button_height)
    apply_button_rect = pygame.Rect(apply_button_position_x, apply_button_position_y, apply_button_width, apply_button_height)
    fps_text_rect = pygame.Rect(fps_text_position_x, fps_text_position_y, fps_text_width, fps_text_height)
    open_file_dialog_button_rect = pygame.Rect(open_file_dialog_button_position_x, open_file_dialog_button_position_y, open_file_dialog_button_width, open_file_dialog_button_height)
    volume_button_rect = pygame.Rect(volume_button_position_x, volume_button_position_y, volume_button_width, volume_button_height)
    increase_volume_button_rect = pygame.Rect(increase_volume_button_position_x, increase_volume_button_position_y, increase_volume_button_width, increase_volume_button_height)
    decrease_volume_button_rect = pygame.Rect(decrease_volume_button_position_x, decrease_volume_button_position_y, decrease_volume_button_width, decrease_volume_button_height)
    how_to_button_rect = const.choice_Info_button.move(screen_width//28, 0)
    directory_playlist_button_rect = pygame.Rect(directory_playlist_button_position_x, directory_playlist_button_position_y, directory_playlist_button_width, directory_playlist_button_height)

    font = pygame.font.SysFont(None, 30)

    if const.fps_show:
        show_fps_button_text = "Yes"
    else:
        show_fps_button_text = "No"

    new_playlist = None
    while running:
        const.screen.fill(const.green)
        events = pygame.event.get()
        utils.change_music_volume()
        mouse_pos = pygame.mouse.get_pos()

        draw_functions.draw_button(const.screen, const.blue, show_fps_button_rect, show_fps_button_text, font, const.black, mouse_pos)
        back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height = draw_functions.load_icons(const.screen, back_icon_path, back_icon_width, back_icon_height, back_icon_position_x, back_icon_position_y)
        back_icon_rect = pygame.Rect(back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height)
        draw_functions.draw_button(const.screen, const.blue, apply_button_rect, "Apply", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, open_file_dialog_button_rect, "Load new playlist", font, const.black, mouse_pos)
        draw_functions.draw_text(const.screen, "Show FPS counter:", const.black, fps_text_rect, font, line_spacing = 5)
        if const.playlist:
            song_path = const.playlist[const.current_song_index]
            song_name = os.path.basename(song_path)
        else:
            song_name = " "
        draw_functions.draw_centered_text_with_other_element_as_reference_point(const.screen, f"Current song: {song_name}", font, const.black, open_file_dialog_button_rect, x_offset=20)
        draw_functions.draw_button(const.screen, const.blue, volume_button_rect, f"{int(const.music_volume * 100)}%", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, increase_volume_button_rect, "+", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, decrease_volume_button_rect, "-", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, how_to_button_rect, "How to?", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, directory_playlist_button_rect, "Directory playlist", font, const.black, mouse_pos)
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
                    const.fps_show = const.fps_apply 
                if  back_icon_rect.collidepoint(mouse_pos):
                    running = False
                    return
                if apply_button_rect.collidepoint(mouse_pos): 
                    if new_playlist:
                        pygame.mixer.music.stop()
                        const.playlist = new_playlist
                        const.current_song_index = 0
                        utils.play_current_song()
                if open_file_dialog_button_rect.collidepoint(mouse_pos):
                    custom_playlist, songs = utils.load_playlist()
                    if custom_playlist:
                        new_playlist = list(songs)
                if increase_volume_button_rect.collidepoint(mouse_pos):
                    if const.music_volume < 1.0:
                        const.music_volume += 0.05
                    else:
                        const.music_volume = 1.0
                if decrease_volume_button_rect.collidepoint(mouse_pos):
                    if const.music_volume > 0.0:
                        const.music_volume -= 0.05
                    else:
                        const.music_volume = 0.0
                if how_to_button_rect.collidepoint(mouse_pos):
                    draw_functions.draw_message_box("How to use settings", text_messages.how_to_text)
                if directory_playlist_button_rect.collidepoint(mouse_pos):
                    custom_playlist, songs = utils.load_playlist()
                    if custom_playlist:
                        new_playlist = list(songs)
                        utils.copy_songs_to_directory(new_playlist)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)