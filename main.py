def on_on_overlap(sprite, otherSprite):
    electrode.x = randint(0, scene.screen_width())
    electrode.y = randint(0, scene.screen_height())
    info.change_score_by(1)
    info.start_countdown(5)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

electrode: Sprite = None
scene.set_background_color(7)
ditto = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . f f 3 3 3 f f . . . . . 
            . . . f f 3 3 3 3 3 f f f . . . 
            . . f 3 3 3 f 3 f 3 3 3 f f . . 
            . f f 3 3 3 3 3 3 3 3 3 f f . . 
            . f 3 3 3 3 2 2 2 3 3 3 f . . . 
            . f f f 3 3 3 3 3 3 3 3 f f . . 
            . . . f 3 3 3 3 3 3 3 3 3 f . . 
            . . f f 3 3 3 3 3 3 3 3 3 f . . 
            . f f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f f f f f f f f f f f 3 f . . 
            . . f f . . f f . f f f f f . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(ditto)
electrode = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f . f f f . . . . 
            . . . . 1 f 1 f 1 f 1 f 1 . . . 
            . . . . 1 1 1 1 1 1 1 1 1 . . . 
            . . . 1 1 1 f 1 1 1 f 1 1 1 . . 
            . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . . 2 2 2 f 1 f 1 f 2 2 2 . . 
            . . . . 2 2 2 1 f 1 f 2 2 . . . 
            . . . . 2 2 2 2 2 2 2 2 2 . . . 
            . . . . . . 2 2 2 2 2 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)