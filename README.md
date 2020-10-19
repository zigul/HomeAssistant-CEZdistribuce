# CEZ Distribuce - Home Assistant Sensor

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This sensor is downloading data from https://www.cezdistribuce.cz/cs/pro-zakazniky/spinani-hdo.html. The integration needs the **region** and the **code**. One can get this information from the contract with CEZ CZ or https://www.cezdistribuce.cz/cs/pro-zakazniky/spinani-hdo.html.
The **region** and the **code** have to be defined in configuration.yaml


This sensor shows
- current state of HDO

## Installation

### Step 1: Download files

#### Option 1: Via HACS

Make sure you have HACS installed. If you don't, run `curl -sfSL https://hacs.xyz/install | bash -` in HA.
Then choose Components under HACS. Choose the menu in the upper right, and select Custom repositories. Then add this repo's URL. You should be able to choose to Install now.

#### Option 2: Manual
Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory.

### Step 2: Configure
Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry for showing current HDO state
binary_sensor:
  - platform: cezdistribuce
    name: nizky tarif
    region: regionStred
    code: A1B5DP6
```
set your **region** and **code**

### Step 3: Restart HA
For the newly added integration to be loaded, HA needs to be restarted.


## References
- PRE Distribuce - Home Assistant Sensor (https://github.com/slesinger/HomeAssistant-PREdistribuce)