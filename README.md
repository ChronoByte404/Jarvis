# Jarvis
My personal AI, capable of local computer control and discord server auto-moderation.

Jarvis has two conversation modes - Random and Fixed - Random utilises the JanexBot library to generate responses and save inputs to reuse in conversations, but isn't 100% efficient as it starts with a relatively small database, where as Fixed is simply an intent classifier which ensures the appropriate responses are given in return.

Before usage, you need a discord bot key stored in discord_key.json, stored in the 'Settings' subdirectory. Once you create that, you're good to go.

## Setting up

Clone Jarvis' repository.

```bash
gh repo clone Cipher58/Jarvis
cd Jarvis
```

To ensure that your version of Jarvis is in-sync with my version on a fundamental level, I would recommend activating one of the built-in virtual environments.

### Ubuntu
```
source VE/Ubuntu/bin/activate
```

### Ubuntu-derived Linux

```bash
source VE/LinuxEnv/bin/activate
```

### MacOS

```bash
source VE/MacEnv/bin/activate
```

If you do not see your OS-supported Virtual Environment, you either use Windows or you can create a virtual environment using venv.
```bash
python3 -m venv VE/(name)

source VE/(name)/bin/activate

python3 -m pip install -r Setup/requirements.txt
```

Due to storage limitations on Github, these virtual environments do not have the dependencies pre-installed. So after activating your Virtual Environment, you can install the dependencies in one go using this command.


```bash
python3 -m pip install -r ./Setup/requirements.txt
```

## Activating Jarvis

Jarvis' AI part exists as a backend which runs a server on a localhost 8000 port. You'll need to activate that first with the following command.

```bash
python3 main.py server
```

Then, open a new tab, you'll have a choice of interfaces to use. If you don't specify one when you run the first command, it'll ask you for one upon boot-up.

```bash
python3 main.py whisper/basic/discord
```

The fail-safe will automatically copy the json files from your Templates folder into a new one called "Settings" which will allow Jarvis to boot up smoothly without you needing to do it manually.

## Jarvis' face

Jarvis' circular face will appear if the boot-up is successful, and with a pre-trained .pth model, the intent classifier should work.

I hope this short README comes in useful.
