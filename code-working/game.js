// Utility function to initialize a flow network
function createFlowNetwork(fields, waterSupply) {
    let graph = {};
    fields.forEach(field => {
        graph[field.name] = {
            value: field.cropValue,
            waterRequirement: field.waterRequirement,
            soilQuality: field.soilQuality,
            waterReceived: 0 // Initially no water assigned
        };
    });
    graph['source'] = { waterSupply: waterSupply };
    return graph;
}

// Ford-Fulkerson algorithm for maximizing water distribution
function maxWaterFlow(graph, source, fields) {
    let totalWaterDistributed = 0;

    // Simulate distributing water to fields
    for (let field of fields) {
        let availableWater = Math.min(graph['source'].waterSupply, graph[field.name].waterRequirement);
       
        // Prioritize fields with higher value crops
        if (availableWater > 0 && graph[field.name].soilQuality > 50) { // Soil quality threshold
            graph[field.name].waterReceived = availableWater;
            totalWaterDistributed += availableWater;
            graph['source'].waterSupply -= availableWater;
        }
    }

    return totalWaterDistributed;
}

// Dynamic adjustment based on weather/soil changes
function adjustWaterDistribution(graph, weatherCondition) {
    let adjustmentFactor = weatherCondition === 'rainy' ? 0.8 : 1.2; // Reduce water on rainy days, increase on hot days
    for (let field in graph) {
        if (field !== 'source') {
            graph[field].waterReceived *= adjustmentFactor;
        }
    }
}

// Example usage
let fields = [
    { name: 'FieldA', cropValue: 100, waterRequirement: 500, soilQuality: 60 },
    { name: 'FieldB', cropValue: 80, waterRequirement: 300, soilQuality: 55 },
    { name: 'FieldC', cropValue: 50, waterRequirement: 200, soilQuality: 40 }
];

let waterSupply = 800;
let graph = createFlowNetwork(fields, waterSupply);

// Initial water distribution
let totalWater = maxWaterFlow(graph, 'source', fields);
console.log('Total water distributed:', totalWater);
console.log('Water distribution:', graph);

// Adjust distribution based on changing weather
adjustWaterDistribution(graph, 'hot');
console.log('Adjusted water distribution:', graph);