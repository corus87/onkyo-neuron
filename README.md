# Onkyo
Onkyo neuron for Kalliope
## Synopsis

Onkyo eISCP Control

## Installation
```bash
kalliope install --git-url https://github.com/corus87/onkyo-neuron
```

## Options

| parameter   | required   | default      | choices   | comments                            |
|-------------|------------|--------------|-----------|-------------------------------------|
| ip_address  | yes        | None         | string    | The ip address of your onkyo        |
| volume      | no         | None         | integer   |                                     |
| command_1   | no         | None         | string    | see eiscp-commands.yaml for commands|
| command_2   | no         | None         | string    |                                     |
| command_3   | no         | None         | string    |                                     |
| command_4   | no         | None         | string    |                                     |
| command_5   | no         | None         | string    |                                     |
| command_6   | no         | None         | string    |                                     |

## Synapses example
```
  - name: "onkyo-volume"
    signals:  
      - order: "set volume to {{ query }}"    
    neurons:
      - onkyo:
          ip_address: 192.168.0.120
          volume: "{{ query }}"
  
  - name: "onkyo-mute"
    signals:  
      - order: "mute onkyo"
    neurons:
      - onkyo:
          ip_address: 192.168.0.120
          command_1: "audio-muting=on"
  
  - name: "onkyo-power-off"
    signals:  
      - order: "turn off onkyo"  
    neurons:
      - onkyo:
          ip_address: 192.168.0.120
          command_1: "system-power=standby"
 
 - name: "onkyo-volume-up"
    signals:
      - order: "turn up the music"
    neurons:
      - onkyo:
          ip_address: 192.168.0.120
          command_1: "volume=level-up"
          command_2: "volume=level-up"
          command_3: "volume=level-up"
          command_4: "volume=level-up"
```
