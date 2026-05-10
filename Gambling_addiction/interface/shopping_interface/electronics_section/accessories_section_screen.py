import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages
import classes.items_class as items_class

def accessories_section_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    font = pygame.font.SysFont(None, 30)
    
    accessory_1 = items_class.shop_item("electronics", "icons\\acc_icon_1.png", "accessory", 129)
    accessory_2 = items_class.shop_item("electronics", "icons\\acc_icon_2.png", "accessory", 35)
    accessory_3 = items_class.shop_item("electronics", "icons\\acc_icon_3.png", "accessory", 49)
    accessory_4 = items_class.shop_item("electronics", "icons\\acc_icon_4.png", "accessory", 79)
       
    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        utils.play_music()

        info_text = "Balance:" + str(const.balance)

        const.screen.fill(const.acc_bckgd)

        draw_functions.draw_title(const.screen, const.white, "ACCESSORIES SECTION")
        draw_functions.draw_text(const.screen, info_text, const.white, const.text_rect, font,line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        draw_functions.draw_button(const.screen, const.acc_bckgd, const.buy_Info_button, "Buy Info", font, const.white)
        if const.buy_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]: 
                draw_functions.draw_message_box('Buy info', text_messages.buy_text)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\electronics_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_ELECTRONICS)
       
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, accessory_1.image_path, icon_width_screen, icon_height_screen, position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, accessory_1.item_price, accessory_1)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, accessory_2.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, accessory_2.item_price, accessory_2)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, accessory_3.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, accessory_3.item_price, accessory_3)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, accessory_4.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, accessory_4.item_price, accessory_4)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
                
        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.white, const.fps_rect, font, const.fps,  const.line_spacing)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)