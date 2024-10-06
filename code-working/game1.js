// Function to generate and update dungeon map using a Voronoi diagram
class DungeonMap {
    constructor() {
        this.map = []; // Array to store regions and explored areas
        this.treasures = []; // Store the positions of treasure rooms
    }

    // Function to generate Voronoi regions for the dungeon
    generateVoronoiRegions(center, radius) {
        const newRegion = { center, radius, type: 'empty' }; // Empty region by default

        // Strategically place treasures in some regions
        if (Math.random() > 0.8) {
            newRegion.type = 'treasure'; // 20% chance to place a treasure
            this.treasures.push(newRegion.center); // Mark treasure location
        }

        this.map.push(newRegion);
    }

    // Function to dynamically update the dungeon as the player explores new areas
    updateMap(playerPosition) {
        const explorationRadius = 5; // Define how far the player can explore at once

        // Check for unexplored areas around the player and generate new regions
        for (let x = playerPosition.x - explorationRadius; x <= playerPosition.x + explorationRadius; x++) {
            for (let y = playerPosition.y - explorationRadius; y <= playerPosition.y + explorationRadius; y++) {
                // If the area has not been explored yet, generate a new region
                if (!this.isExplored(x, y)) {
                    this.generateVoronoiRegions({ x, y }, explorationRadius);
                }
            }
        }
    }

    // Helper function to check if an area is already explored
    isExplored(x, y) {
        return this.map.some(region => region.center.x === x && region.center.y === y);
    }
}

// Example usage
const dungeon = new DungeonMap();
const playerPosition = { x: 0, y: 0 };

// Initial map generation at the start
dungeon.updateMap(playerPosition);
console.log("Initial Dungeon Map:", dungeon.map);

// As the player moves and explores new areas
playerPosition.x = 10; // Player moves to a new area
dungeon.updateMap(playerPosition);
console.log("Updated Dungeon Map:", dungeon.map);