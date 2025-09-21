# Space Invaders - Sprite Requirements

This document lists all the sprite images that need to be created and uploaded to the `sprites/` folder for the Space Invaders game.

## Directory Structure
All sprites should be placed in the `sprites/` directory in the project root.

## Required Sprite Images (8 total)

### 1. Player Ship
- **Filename**: `player_ship.png`
- **Purpose**: Main player spaceship
- **Recommended Size**: 50x30 pixels
- **Format**: PNG with transparency
- **Description**: Classic spaceship design, facing upward
- **Color Scheme**: Green/blue tones to match the original game

### 2. Enemy Invaders (3 Types)

#### Type 1 Invader (Top Row)
- **Filename**: `invader_type1.png`
- **Purpose**: Highest value enemy invaders
- **Recommended Size**: 40x25 pixels
- **Format**: PNG with transparency
- **Description**: Small, compact alien design
- **Color Scheme**: Red/orange tones
- **Points Value**: Highest (typically 30 points)

#### Type 2 Invader (Middle Row)
- **Filename**: `invader_type2.png`
- **Purpose**: Medium value enemy invaders
- **Recommended Size**: 40x25 pixels
- **Format**: PNG with transparency
- **Description**: Medium-sized alien with distinctive features
- **Color Scheme**: Yellow/orange tones
- **Points Value**: Medium (typically 20 points)

#### Type 3 Invader (Bottom Row)
- **Filename**: `invader_type3.png`
- **Purpose**: Lowest value enemy invaders
- **Recommended Size**: 40x25 pixels
- **Format**: PNG with transparency
- **Description**: Larger, bulkier alien design
- **Color Scheme**: Green/cyan tones
- **Points Value**: Lowest (typically 10 points)

### 3. Projectiles

#### Player Bullet
- **Filename**: `bullet_player.png`
- **Purpose**: Projectile fired by the player
- **Recommended Size**: 6x15 pixels
- **Format**: PNG with transparency
- **Description**: Thin, vertical projectile
- **Color Scheme**: Bright yellow/white
- **Animation**: Static (no animation needed)

#### Enemy Bullet
- **Filename**: `bullet_enemy.png`
- **Purpose**: Projectile fired by enemy invaders
- **Recommended Size**: 6x15 pixels
- **Format**: PNG with transparency
- **Description**: Different design from player bullet
- **Color Scheme**: Red/orange
- **Animation**: Static (no animation needed)

### 4. Background
- **Filename**: `background.png`
- **Purpose**: Game background/starfield
- **Recommended Size**: 800x600 pixels (full screen)
- **Format**: PNG or JPG
- **Description**: Space background with stars
- **Color Scheme**: Dark blue/black with white stars
- **Style**: Can be static starfield or subtle nebula

### 5. Explosion Effect
- **Filename**: `explosion.png`
- **Purpose**: Visual effect when projectiles collide
- **Recommended Size**: 20x20 pixels
- **Format**: PNG with transparency
- **Description**: Small explosion/spark effect
- **Color Scheme**: Bright colors (white, yellow, orange, red)
- **Animation**: Static sprite (expansion handled by code)

## Technical Specifications

### General Requirements
- **File Format**: PNG preferred for sprites with transparency, JPG acceptable for background
- **Color Depth**: 32-bit RGBA for PNG files
- **Transparency**: Use alpha channel for transparent backgrounds
- **Compression**: Optimize file sizes while maintaining quality

### Design Guidelines
- **Pixel Art Style**: Maintain retro pixel art aesthetic
- **Contrast**: Ensure good contrast against dark space background
- **Consistency**: All sprites should have consistent art style
- **Clarity**: Sprites should be clearly visible at their intended sizes

### Fallback Behavior
The game includes fallback mechanisms:
- If sprites are missing, colored rectangles will be displayed
- Player ship: Green rectangle (0, 255, 0)
- Enemy invaders: Red rectangle (255, 0, 0)
- Player bullets: Yellow rectangle (255, 255, 0)
- Enemy bullets: Light red rectangle (255, 100, 100)
- Background: Black fill (0, 0, 0)
- Explosion effect: Concentric colored circles (white, yellow, orange, red)

## Optional Enhancements (Future)
These sprites are not currently implemented but could be added:
- Explosion animations
- Power-up items
- UFO bonus enemy
- Particle effects
- Animated sprites with multiple frames

## File Naming Convention
- Use lowercase letters
- Use underscores for spaces
- Include file extension (.png or .jpg)
- Be descriptive but concise

## Testing
After adding sprites:
1. Run the game to verify all sprites load correctly
2. Check that fallback rectangles appear for missing sprites
3. Verify sprite positioning and scaling
4. Test game performance with loaded sprites

## Notes
- The game automatically scales sprites to the specified dimensions
- Sprites are cached after first load for better performance
- Error handling displays console warnings for missing sprites
- All sprites should maintain the classic Space Invaders aesthetic
