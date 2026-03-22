import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages
import classes.items_class as items_class

def hand_tools_section_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    font = pygame.font.SysFont(None, 30)

    hand_tool_1 = items_class.shop_item("tools", "icons\\hand_tool_icon_1.png", "hand tool", 29)
    hand_tool_2 = items_class.shop_item("tools", "icons\\hand_tool_icon_2.png", "hand tool", 12)
    hand_tool_3 = items_class.shop_item("tools", "icons\\hand_tool_icon_3.png", "hand tool", 35)
    hand_tool_4 = items_class.shop_item("tools", "icons\\hand_tool_icon_4.png", "hand tool", 42)
 
    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()

        info_text = "Balance:" + str(const.balance)

        const.screen.fill(const.store_bckgd)

        draw_functions.draw_title(const.screen, const.black, "HAND TOOLS SECTION")
        draw_functions.draw_text(const.screen, info_text, const.black, const.text_rect, font,line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        draw_functions.draw_button(const.screen, const.store_bckgd, const.buy_Info_button, "Buy Info", font, const.black)
        if const.buy_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]: 
                draw_functions.draw_message_box('Buy info', text_messages.buy_text)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\tools_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TOOLS)
       
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hand_tool_1.image_path, icon_width_screen, icon_height_screen, position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, hand_tool_1.item_price, hand_tool_1)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hand_tool_2.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, hand_tool_2.item_price, hand_tool_2)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hand_tool_3.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, hand_tool_3.item_price, hand_tool_3)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, hand_tool_4.image_path, icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.buy(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, hand_tool_4.item_price, hand_tool_4)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y - 15)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
                
        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, const.fps_rect, font, const.fps, const.line_spacing)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)