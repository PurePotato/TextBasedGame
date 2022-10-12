import time

# Caitlyn Murphy
rooms = {  # dictionary of rooms with directions
    'Great Hall': {
        'East': 'Botanical Room',
        'West': 'Kitchen',
        'South': {
            'Left': 'Corridor',
            'Right': 'Library'
        }
    },
    'Kitchen': {
        'East': 'Great Hall',
        'South': 'Dining Room'
    },
    'Dining Room': {
        'North': 'Kitchen',
        'South': 'Wine Cellar'
    },
    'Wine Cellar': {
        'North': 'Dining Room'
    },
    'Botanical Room': {
        'West': 'Great Hall',
        'South': 'Alchemy Room'
    },
    'Alchemy Room': {
        'North': 'Botanical Room'
    },
    'Library': {
        'North': 'Great Hall'
    },
    'Corridor': {
        'North': 'Great Hall',
        'East': 'Bedchambers',
        'South': 'Study'
    },
    'Study': {
        'North': 'Corridor'
    },
    'Bedchambers': {
        'West': 'Corridor'
    }
}

items = {  # dictionary of items per room
    'Great Hall': 'empty',
    'Kitchen': 'Turkey Jerky',
    'Dining Room': 'Shield',
    'Wine Cellar': 'Horned Helmet',
    'Botanical Room': 'Boots',
    'Alchemy Room': 'Healing Potion',
    'Library': 'Beastiary',
    'Corridor': 'Chest plate',
    'Study': 'Iron Sword',
    'Bedchambers': 'Fire Giant'
}


# basic method to show the instructions at the beginning of the game
def show_instruction():
    print('Dragon Text Adventure Game')
    print('aka text-based D&D')
    print('Collect 8 items before finding the Fire Giant, or be eaten by him.')
    print('Move commands: go East, go West, go South, go North')
    print("Add items to inventory: pick up 'item name'\n")


# method to determine where you are in the game
# if in bedchambers and have all items then defeat villain
# if in bedchamber and not have all items then lose to villain
# if in neither of those then tell what room and current inventory
def current_status(current_room, inventory_list):
    if current_room == 'Bedchambers' and len(inventory_list) == 8:
        print('As you open the door, you see a Fire Giant in the room.')
        time.sleep(2.5)
        print('After a long fight, you defeat the Fire Giant and claim victory!')
        exit()
    elif current_room == 'Bedchambers' and len(inventory_list) != 8:
        print('Oh no! Adventurer you did not pick up all of the required items!')
        print('The Fire Giant slices you across the chest. You succumb to the pain...')
        exit()
    else:
        print(f'You are in the {current_room}')
        print(f'Inventory: {inventory_list}')
    print(f'_________________________')


# method to pickup the item
def obtain_item(current_room):
    item = items[current_room]  # gets what item should be in this oom
    pickup_item = input(f'Please use the command to pick up {item}: ')
    # print(pickup_item[8:])
    if pickup_item[8:] == item:
        if items[current_room] not in inventory_list:
            inventory_list.append(items[current_room])
        else:
            print('Invalid command.')
    else:
        print('Invalid item.')


current_room = 'Great Hall'
inventory_list = []

if __name__ == '__main__':
    show_instruction()
    while True:
        current_status(current_room, inventory_list)
        # checks if the item in current room is in the inventory list before printing the item
        if items[current_room] in inventory_list:
            print(f'Item currently in room: {items["Great Hall"]}')
        else:
            print(f'Item currently in room: {items[current_room]}')
        # choice to move or pick up item
        item_or_move = input(
            "Would you like to move or pick up an item?\nUse 'move' to move or 'item' to pick up an item:")
        if item_or_move == 'item':
            obtain_item(current_room)
        elif item_or_move == 'move':
            direction = input('Which way do you want to go?\n')
            # exits game
            if direction == 'Exit':
                exit()
            # determines if the room has a special direction check

            if (direction == 'East' or direction == 'West' or
                    direction == 'North' or direction == 'South' and current_room != 'Great Hall'):
                new_room = current_room
                for room_name in rooms:
                    if room_name == current_room:
                        if direction in rooms[room_name]:
                            new_room = rooms[room_name][direction]
                current_room = new_room
            # based on my map, the great hall has two ways south so this handles that
            elif current_room == 'Great Hall' and direction == 'South':
                print('There are two doors to the South.')
                gh_south = input('Would you like to go to the left door or the right door?\n')
                new_room = current_room
                for room_name in rooms:
                    if room_name == current_room:
                        if direction in rooms[room_name]:
                            if gh_south in rooms[room_name][direction]:
                                new_room = rooms[room_name][direction][
                                    gh_south]  # figuring this out made me feel amazing. multilevel dictionaries are cool now
                current_room = new_room

            else:
                print('Invalid direction.')
        else:
            print('Invalid choice.')
