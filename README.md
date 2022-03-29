# House Automation Example

A simple example of a home automation code, using python 3.10 features and asyncio

## Applcation Flow

1. The Controller is the core of the application
2. A Device must register itself to the Controller
3. Device must implement at least 3 functions (A "contract" will be provided)
4. Another contract of command types will be provided to communicate with the Controller

## Python used features

- Dataclass to act as a command contract
- Abstract Classes to work as a Device Contract
- Asyncio (2nd step) to allow asynchronous control of the devices
- Typing (lib) will allow extensions to validate your code and correct linting it and create a more readable code

## TODOs

### MVP - Sequential execution for a Light bulb control

- [x] Build skeleton project

- **COMMAND:**
  - [x] Create events that will be accepted for the Controller
  - [x] Create default command entity
- **DEVICE:**
  - [x] Create Device Contract
    - must have a connect method
    - must have a disconnect method
    - must have a send command method
  - [x] Implement Light bulb entity
- **CONTROLLER:**
  - [x] Create Controller entity
    - it should generate id for the device
    - it should control active devices
    - it should call commands on defined devices
- **NEW DEVICE - EchoDot:**
  - [ ] Create an EchoDot device
    - it should play music
    - it should look for the weather
