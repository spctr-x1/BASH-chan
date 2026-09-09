# bash-chan CLI

> A tsundere Linux shell wrapper that reacts to your commands.

## Functions

Simply put, this shell wrapper allows you to work in your BASH terminal as normal, but with a tsundere companion to keep you company during your work. She will respond to your commands, and is made to respond according to the command sent as well as the result. In the future, I hope to add more feature, like minigames or ascii visuals to show the various reactions bash chan can give off.

## Quick Start

Make the wrapper executable:

```bash
chmod +x bash-chan
```

Run a command:

```bash
./bash-chan echo "hello world!"
```

Example output:

```text
hello, world

[ bash-chan ] Hmph. It worked. Don't look so pleased with yourself.
```

## Interactive Mode

Run `bash-chan` without a command to open an interactive session:

```bash
./bash-chan
```

Then enter commands at the `bash-chan [/your/current/directory]>` prompt. The directory shown in the prompt updates as your working directory changes. Use `exit`, `quit`, `Ctrl-D`, or `Ctrl-C` to leave.

## Shell Compatibility

Commands are passed through a shell, so regular shell syntax and flags work:

```bash
./bash-chan sh -c 'exit 1'
./bash-chan git --version
./bash-chan find . -name '*.py'
```

The wrapper returns the same exit code as the command it ran:

```bash
./bash-chan make && echo "build passed"
```

## Install For Your User

Create a personal command link:

```bash
mkdir -p ~/.local/bin
ln -s "$PWD/bash-chan" ~/.local/bin/bash-chan
```

Make sure `~/.local/bin` is included in your `PATH`, then run it from anywhere:

```bash
bash-chan pwd
```

## Project Status

This is a lightweight prototype focused on personality-driven command feedback. The command execution path stays deliberately small, while the reaction catalog can grow independently as more Bash workflows are added.
