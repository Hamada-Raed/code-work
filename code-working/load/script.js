class Machine {
    constructor(consumption) {
        this.consumption = consumption;
        this.on = true;
    }

    toggle() {
        this.on = !this.on;
    }

    getConsumption() {
        return this.on ? this.consumption : 0;
    }
}

function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function generateGrid(machineCount) {
    const machinePositions = [];
    for (let i = 0; i < machineCount; i++) {
        machinePositions.push({ row: Math.floor(Math.random() * 4), col: Math.floor(Math.random() * 4) });
    }
    return machinePositions;
}

function displayGrid(machinePositions) {
    const grid = document.getElementById('grid');
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const cell = document.createElement('div');
            const machineIndex = machinePositions.findIndex(position => position.row === i && position.col === j);
            if (machineIndex !== -1) {
                cell.classList.add('machine');
                cell.addEventListener('click', () => toggleMachine(machineIndex));
            } else {
                cell.classList.add('empty');
            }
            grid.appendChild(cell);
        }
    }
}

function generateConsumptions(machineCount) {
    const consumptions = [];
    for (let i = 0; i < machineCount; i++) {
        consumptions.push(Math.floor(Math.random() * 100));
    }
    return consumptions;
}

function updateTotalLoad(machines) {
    const totalLoad = machines.reduce((a, b) => a + b.getConsumption(), 0);
    const totalLoadElement = document.getElementById('totalLoad');
    totalLoadElement.innerText = `Total Electricity Load: ${totalLoad}W`;
    if (totalLoad > 100) {
        totalLoadElement.style.color = 'red';
    } else {
        totalLoadElement.style.color = 'green';
    }
}

function toggleMachine(index) {
    machines[index].toggle();
    updateMachineCosts();
    updateTotalLoad(machines);
}

function updateMachineCosts() {
    const machineCostsElement = document.getElementById('machineCosts');
    machineCostsElement.innerHTML = '';
    machines.forEach((machine, index) => {
        const cost = machine.getConsumption() * 10;
        const costElement = document.createElement('p');
        costElement.innerText = `Machine ${index + 1}: ${cost}$`;
        machineCostsElement.appendChild(costElement);
    });
}

function controlMachineStatus(machines) {
    const totalLoad = machines.reduce((a, b) => a + b.getConsumption(), 0);
    if (totalLoad > 200) {
        const maxConsumptionMachine = machines.reduce((a, b) => a.getConsumption() > b.getConsumption() ? a : b);
        maxConsumptionMachine.toggle();
    }
}

function toggleAllMachines() {
    machines.forEach(machine => machine.toggle());
    updateMachineCosts();
    updateTotalLoad(machines);
}

const machineCount = parseInt(getParameterByName('machineCount'));
const machinePositions = generateGrid(machineCount);
const consumptions = generateConsumptions(machineCount);
const machines = consumptions.map(consumption => new Machine(consumption));
displayGrid(machinePositions);
updateTotalLoad(machines);
updateMachineCosts();
setInterval(() => controlMachineStatus(machines), 1000);
const toggleAllButton = document.getElementById('toggleAll');
toggleAllButton.addEventListener('click', toggleAllMachines);