
"use strict";

let GetMaterialLocations = require('./GetMaterialLocations.js')
let SubmitTray = require('./SubmitTray.js')
let ConveyorBeltControl = require('./ConveyorBeltControl.js')
let AGVControl = require('./AGVControl.js')
let PopulationControl = require('./PopulationControl.js')
let VacuumGripperControl = require('./VacuumGripperControl.js')

module.exports = {
  GetMaterialLocations: GetMaterialLocations,
  SubmitTray: SubmitTray,
  ConveyorBeltControl: ConveyorBeltControl,
  AGVControl: AGVControl,
  PopulationControl: PopulationControl,
  VacuumGripperControl: VacuumGripperControl,
};
