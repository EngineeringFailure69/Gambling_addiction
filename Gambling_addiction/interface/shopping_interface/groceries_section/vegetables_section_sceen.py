import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import classes.items_class as items_class
import text_messages as text_messages
import settings.sound_settings as sound_settings

def vegetables_section_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    font = pygame.font.SysFont(None, 30)

    vegetable_1 = items_class.shop_item("groceries", "assets\\icons\\shopping_icons\\vegetables_icon_1.png", "vegetables", 0.25)
    vegetable_2 = items_class.shop_item("groceries", "assets\\icons\\shopping_icons\\vegetables_icon_2.png", "vegetables", 0.75)
    vegetable_3 = items_class.shop_item("groceries", "assets\\icons\\shopping_icons\\vegetables_icon_3.png", "vegetables", 0.30)
    vegetable_4 = items_class.shop_item("groceries", "assets\\icons\\shopping_icons\\vegetables_icon_4.png", "vegetables", 0.40)
       
    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        sound_settings.play_music()

        info_text = "Balance:" + str(const.balance)

        const.screen.fill(const.vegetables_bckgd)

        draw_functions.draw_title(const.screen, const.store_text, "VEGETABLES SECTION")
        draw_functions.draw_text(const.screen, info_text, const.black, const.text_rect, font,line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        draw_functions.draw_button(const.screen, const.vegetables_bckgd, const.buy_Info_button, "Buy Info", font, const.black)
        if const.buy_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]: 
                draw_functions.draw_message_box('Buy info', text_messages.buy_text)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icons\\groceries_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_GROCERIES)
       
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, vegetable_1.image_path, icon_width_screen, icon_height_screen, position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, vegetable_1.item_price, vegetable_1)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, vegetable_2.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, vegetable_2.item_price, vegetable_2)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, vegetable_3.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, vegetable_3.item_price, vegetable_3)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, vegetable_4.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, vegetable_4.item_price, vegetable_4)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path_old, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
                
        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, const.fps_rect, font, const.fps, const.line_spacing)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)