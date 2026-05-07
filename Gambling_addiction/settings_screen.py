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

    back_icon_path = "icons\\go_back_icon2.png"
    back_icon_position_x = screen_width / 25
    back_icon_position_y = screen_height / 29 
    back_icon_width = 40
    back_icon_height = 30

    how_to_button_text = "How to?"
    how_to_button_width = screen_width / 9.3333333333
    how_to_button_height = screen_height / 20
    how_to_button_position_x = screen_width - how_to_button_width - screen_width / 23.333333333
    how_to_button_position_y = back_icon_position_y

    settings_screen_bckgd_icon_width = screen_width / 1.1666666667 
    settings_screen_bckgd_icon_height = screen_height 
    settings_screen_bckgd_icon_position_x = screen_width / 14 
    settings_screen_bckgd_icon_position_y = screen_height / 60 
    settings_screen_bckgd_icon_path = "icons\\settings_screen_bckgd_icon.png"

    style_button_width = screen_width * 0.6
    style_button_height = screen_height / 10
    style_button_position_x = screen_width / 2 - style_button_width / 2
    style_button_position_y = screen_height / 3.8

    fps_text_width = style_button_width / 4.2 
    fps_text_height = style_button_height / 2 
    fps_text_position_x = style_button_position_x + style_button_width / 12 
    fps_text_position_y = style_button_position_y + fps_text_height / 2 + style_button_height / 10
    fps_text = "Show FPS counter"

    show_fps_button_height = style_button_height / 2 
    show_fps_button_width = style_button_width / 5.6  
    show_fps_button_position_x = style_button_position_x + style_button_width - show_fps_button_width - style_button_width / 28 
    show_fps_button_position_y = fps_text_position_y - show_fps_button_height / 6
    show_fps_button_text = ""

    fps_speed_icon_width = style_button_width / 14 
    fps_speed_icon_height = style_button_height 
    fps_speed_icon_position_x = style_button_position_x + style_button_width / 180
    fps_speed_icon_position_y = style_button_position_y + style_button_height / 20
    fps_speed_icon_path = "icons\\fps_speed_icon.png"

    open_file_dialog_button_height = style_button_height / 2 
    open_file_dialog_button_width = style_button_width / 4.2 
    open_file_dialog_button_position_x = fps_text_position_x 
    open_file_dialog_button_position_y = fps_text_position_y + style_button_height + screen_height // 12 - style_button_height / 12 
    open_file_dialog_button_text = "Load new playlist"

    open_file_dialog_icon_width = fps_speed_icon_width - style_button_width / 280
    open_file_dialog_icon_height = fps_speed_icon_height - style_button_height / 12
    open_file_dialog_icon_position_x = fps_speed_icon_position_x
    open_file_dialog_icon_position_y = style_button_position_y + style_button_height + screen_height // 12 + style_button_height / 24
    open_file_dialog_icon_path = "icons\\load_playlist_icon.png"

    volume_button_height = style_button_height / 2 
    volume_button_width = style_button_width / 4.2 
    volume_button_position_x = screen_width / 2 + style_button_width / 7 
    volume_button_position_y = style_button_position_y + style_button_height + screen_height // 12 + screen_height / 9.23 + style_button_height / 4 

    increase_volume_button_height = style_button_height / 2 
    increase_volume_button_width = style_button_width / 16.8 
    increase_volume_button_position_x = volume_button_position_x + volume_button_width + 20
    increase_volume_button_position_y = volume_button_position_y
    increase_volume_button_text = "+"

    decrease_volume_button_height = style_button_height / 2 
    decrease_volume_button_width = style_button_width / 16.8 
    decrease_volume_button_position_x = volume_button_position_x - decrease_volume_button_width - 20
    decrease_volume_button_position_y = volume_button_position_y
    decrease_volume_button_text = "-"

    volume_text_width = style_button_width / 8.4 
    volume_text_height = style_button_height / 2 
    volume_text_position_x = fps_text_position_x 
    volume_text_position_y = volume_button_position_y + style_button_height / 12
    volume_text = "Volume"

    volume_icon_path = "icons\\volume_settings_icon.png"
    volume_icon_width =  open_file_dialog_icon_width
    volume_icon_height = open_file_dialog_icon_height
    volume_icon_position_x = fps_speed_icon_position_x
    volume_icon_position_y = open_file_dialog_icon_position_y + screen_height / 9.23

    directory_playlist_button_width = style_button_width / 1.2 
    directory_playlist_button_height = style_button_height / 2 
    directory_playlist_button_position_x = fps_text_position_x 
    directory_playlist_button_position_y = volume_button_position_y + screen_height / 9.23 
    directory_playlist_button_text = "Directory playlist                                                                          >"

    directory_playlist_icon_width = volume_icon_width
    directory_playlist_icon_height = volume_icon_height
    directory_playlist_icon_position_x = volume_icon_position_x
    directory_playlist_icon_position_y = volume_icon_position_y + screen_height / 9.23
    directory_playlist_icon_path = "icons\\directory_playlist_settings_icon.png"

    apply_button_height = screen_height / 12 
    apply_button_width = screen_width / 7  
    apply_button_position_x = screen_width / 2 - apply_button_width / 2
    apply_button_position_y = screen_height - screen_height / 5.5 
    apply_button_text = "Apply"

    show_fps_button_rect = pygame.Rect(show_fps_button_position_x, show_fps_button_position_y, show_fps_button_width, show_fps_button_height)
    apply_button_rect = pygame.Rect(apply_button_position_x, apply_button_position_y, apply_button_width, apply_button_height)
    fps_text_rect = pygame.Rect(fps_text_position_x, fps_text_position_y, fps_text_width, fps_text_height)
    open_file_dialog_button_rect = pygame.Rect(open_file_dialog_button_position_x, open_file_dialog_button_position_y, open_file_dialog_button_width, open_file_dialog_button_height)
    volume_button_rect = pygame.Rect(volume_button_position_x, volume_button_position_y, volume_button_width, volume_button_height)
    increase_volume_button_rect = pygame.Rect(increase_volume_button_position_x, increase_volume_button_position_y, increase_volume_button_width, increase_volume_button_height)
    decrease_volume_button_rect = pygame.Rect(decrease_volume_button_position_x, decrease_volume_button_position_y, decrease_volume_button_width, decrease_volume_button_height)
    how_to_button_rect = pygame.Rect(how_to_button_position_x, how_to_button_position_y, how_to_button_width, how_to_button_height)
    directory_playlist_button_rect = pygame.Rect(directory_playlist_button_position_x, directory_playlist_button_position_y, directory_playlist_button_width, directory_playlist_button_height)
    style_button_rect = pygame.Rect(style_button_position_x, style_button_position_y, style_button_width, style_button_height)
    volume_text_rect = pygame.Rect(volume_text_position_x, volume_text_position_y, volume_text_width, volume_text_height)

    font = pygame.font.SysFont(None, 30)

    if const.fps_show:
        show_fps_button_text = "Yes"
    else:
        show_fps_button_text = "No"

    new_playlist = None
    background_image_path = "background_photos\\settings_screen_background.png"
    while running:
        const.screen.fill(const.green)
        events = pygame.event.get()
        utils.change_music_volume()
        mouse_pos = pygame.mouse.get_pos()

        draw_functions.load_background_image(const.screen, background_image_path)

        draw_functions.load_icons(const.screen, settings_screen_bckgd_icon_path, settings_screen_bckgd_icon_width, settings_screen_bckgd_icon_height, settings_screen_bckgd_icon_position_x, settings_screen_bckgd_icon_position_y)
        draw_functions.draw_button(const.screen, const.green_settings_button, style_button_rect, "", font, const.golden_settings_button)
        draw_functions.draw_button(const.screen, const.green_settings_button, style_button_rect.move(0, style_button_height + screen_height // 12), "", font, const.golden_settings_button)
        draw_functions.draw_button(const.screen, const.green_settings_button, style_button_rect.move(0, style_button_height + screen_height // 12 + screen_height / 9.23), "", font, const.golden_settings_button)
        draw_functions.draw_button(const.screen, const.green_settings_button, style_button_rect.move(0, style_button_height + screen_height // 12 + screen_height / 9.23 + screen_height / 9.23), "", font, const.golden_settings_button)
        draw_functions.load_icons(const.screen, fps_speed_icon_path, fps_speed_icon_width, fps_speed_icon_height, fps_speed_icon_position_x, fps_speed_icon_position_y)
        draw_functions.load_icons(const.screen, open_file_dialog_icon_path, open_file_dialog_icon_width, open_file_dialog_icon_height, open_file_dialog_icon_position_x, open_file_dialog_icon_position_y)
        draw_functions.load_icons(const.screen, volume_icon_path, volume_icon_width, volume_icon_height, volume_icon_position_x, volume_icon_position_y)
        draw_functions.load_icons(const.screen, directory_playlist_icon_path, directory_playlist_icon_width, directory_playlist_icon_height, directory_playlist_icon_position_x, directory_playlist_icon_position_y)
        draw_functions.draw_button(const.screen, const.lighter_green_settings_button, show_fps_button_rect, show_fps_button_text, font, const.golden_settings_button, mouse_pos)
        back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height = draw_functions.load_icons(const.screen, back_icon_path, back_icon_width, back_icon_height, back_icon_position_x, back_icon_position_y)
        back_icon_rect = pygame.Rect(back_icon_position_x, back_icon_position_y, back_icon_width, back_icon_height)
        draw_functions.draw_button(const.screen, const.green_settings_button, apply_button_rect, apply_button_text, font, const.golden_settings_button, mouse_pos)
        draw_functions.draw_button(const.screen, const.lighter_green_settings_button, open_file_dialog_button_rect, open_file_dialog_button_text, font, const.golden_settings_button, mouse_pos)
        draw_functions.draw_text(const.screen, fps_text, const.golden_settings_button, fps_text_rect, font, line_spacing = 5)
        draw_functions.draw_text(const.screen, volume_text, const.golden_settings_button, volume_text_rect, font, line_spacing = 5)
        if const.playlist:
            song_path = const.playlist[const.current_song_index]
            song_name = os.path.basename(song_path)
        else:
            song_name = " "
        draw_functions.draw_centered_text_with_other_element_as_reference_point(const.screen, f"Current song: {song_name}", font, const.golden_settings_button, open_file_dialog_button_rect, x_offset=20)
        draw_functions.draw_button(const.screen, const.green_settings_button, volume_button_rect, f"{int(const.music_volume * 100)}%", font, const.golden_settings_button)
        draw_functions.draw_button(const.screen, const.lighter_green_settings_button, increase_volume_button_rect, increase_volume_button_text, font, const.golden_settings_button, mouse_pos)
        draw_functions.draw_button(const.screen, const.lighter_green_settings_button, decrease_volume_button_rect, decrease_volume_button_text, font, const.golden_settings_button, mouse_pos)
        draw_functions.draw_button(const.screen, const.green_settings_button, how_to_button_rect, how_to_button_text, font, const.golden_settings_button, mouse_pos)
        draw_functions.draw_button(const.screen, const.lighter_green_settings_button, directory_playlist_button_rect, directory_playlist_button_text, font, const.golden_settings_button, mouse_pos)
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
                    elif const.music_volume - 0.05 < 0.0:
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