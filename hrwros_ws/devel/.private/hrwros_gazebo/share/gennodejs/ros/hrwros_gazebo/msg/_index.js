
"use strict";

let Kit = require('./Kit.js');
let VacuumGripperState = require('./VacuumGripperState.js');
let StorageUnit = require('./StorageUnit.js');
let DetectedObject = require('./DetectedObject.js');
let LogicalCameraImage = require('./LogicalCameraImage.js');
let Order = require('./Order.js');
let KitObject = require('./KitObject.js');
let TrayContents = require('./TrayContents.js');
let Model = require('./Model.js');
let ConveyorBeltState = require('./ConveyorBeltState.js');
let KitTray = require('./KitTray.js');
let PopulationState = require('./PopulationState.js');
let Proximity = require('./Proximity.js');

module.exports = {
  Kit: Kit,
  VacuumGripperState: VacuumGripperState,
  StorageUnit: StorageUnit,
  DetectedObject: DetectedObject,
  LogicalCameraImage: LogicalCameraImage,
  Order: Order,
  KitObject: KitObject,
  TrayContents: TrayContents,
  Model: Model,
  ConveyorBeltState: ConveyorBeltState,
  KitTray: KitTray,
  PopulationState: PopulationState,
  Proximity: Proximity,
};
