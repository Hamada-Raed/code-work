class DungeonMap {
    constructor() {
        this.map = []; 
        this.treasures = []; 
    }

    generateVoronoiRegions(center, radius) {
        const newRegion = { center, radius, type: 'empty' }; 

      
        if (Math.random() > 0.8) {
            newRegion.type = 'treasure'; 
            this.treasures.push(newRegion.center);
        }

        this.map.push(newRegion);
    }

    updateMap(playerPosition) {
        const explorationRadius = 5; 

        for (let x = playerPosition.x - explorationRadius; x <= playerPosition.x + explorationRadius; x++) {
            for (let y = playerPosition.y - explorationRadius; y <= playerPosition.y + explorationRadius; y++) {
                if (!this.isExplored(x, y)) {
                    this.generateVoronoiRegions({ x, y }, explorationRadius);
                }
            }
        }
    }

    isExplored(x, y) {
        return this.map.some(region => region.center.x === x && region.center.y === y);
    }
}

const dungeon = new DungeonMap();
const playerPosition = { x: 0, y: 0 };

dungeon.updateMap(playerPosition);
console.log("Initial Dungeon Map:", dungeon.map);

playerPosition.x = 10; 
dungeon.updateMap(playerPosition);
console.log("Updated Dungeon Map:", dungeon.map);