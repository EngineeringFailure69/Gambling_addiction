import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages
import classes.items_class as items_class

def hatchback_car_section_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, const.screen.get_height() / 17, screen_width, 300)
    font = pygame.font.SysFont(None, 30)

    hatchback_car_1 = items_class.shop_item("car", "icons\\hatchback_car_icon_1.png", "hatchback")
    hatchback_car_2 = items_class.shop_item("car", "icons\\hatchback_car_icon_2.png", "hatchback")
    hatchback_car_3 = items_class.shop_item("car", "icons\\hatchback_car_icon_3.png", "hatchback")
    hatchback_car_4 = items_class.shop_item("car", "icons\\hatchback_car_icon_4.png", "hatchback")

    while running:
        events = pygame.event.get()

        info_text = "Balance:" + str(const.balance)

        const.screen.fill(const.hatchback_bckgd)

        draw_functions.draw_title(const.screen, const.black, "HATCHBACK SECTION")
        draw_functions.draw_text(const.screen, info_text, const.black, text_rect, font,line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        draw_functions.draw_button(const.screen, const.hatchback_bckgd, const.choice_Info_button, "Buy Info", font, const.black)
        if const.choice_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                draw_functions.draw_message_box('Buy info', text_messages.buy_text)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\car_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CARS)
       
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hatchback_car_1.image_path, icon_width_screen, icon_height_screen, position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, 34500, hatchback_car_1)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hatchback_car_2.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, 19200, hatchback_car_2)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hatchback_car_3.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, 26700, hatchback_car_3)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hatchback_car_4.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, 23900, hatchback_car_4)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)