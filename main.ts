sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    electrode.x = randint(0, scene.screenWidth())
    electrode.y = randint(0, scene.screenHeight())
    info.changeScoreBy(1)
    info.startCountdown(5)
})
let electrode: Sprite = null
scene.setBackgroundColor(7)
let ditto = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(ditto)
electrode = sprites.create(img`
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
    `, SpriteKind.Food)
