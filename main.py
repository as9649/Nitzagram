import pygame

from classes.Post import Post
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from helpers import screen
from test_methods import test_comment
from buttons import like_button, comment_button
from helpers import mouse_in_button, read_comment_from_user


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = Post("Images/keawakapu.jpg", "hhhhhhi", "hi2")

    post2 = Post("Images/ronaldo.jpg", "hhhhhhi", "hi2")

    post3 = Post("Images/noa_kirel.jpg", "hhhhhhi", "hi2")

    post4 = Post("Images/montana.jpg", "hhhhhhi", "hi2")

    post_list = [post1, post2, post3, post4]
    print(post1.user_name)
    # TODO: add a post here

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_in_button(like_button, mouse_pos):
                    post1.add_like()
                elif mouse_in_button(comment_button, mouse_pos):
                    comment_text = read_comment_from_user()
                    post1.add_comment(comment_text)

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        post1.display()
        # test_comment()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
