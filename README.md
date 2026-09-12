# bash-chan CLI

A shell wrapper with a cute tsundere who reacts to all your commands in BASH.

## Install

Make the script executable:

```bash
chmod +x main
```

Optionally install it for your user:

```bash
mkdir -p ~/.local/bin
ln -s "$PWD/scripts/main" ~/.local/bin/main
```

Ensure `~/.local/bin` is in `PATH`, then run:

```bash
main
```

When running from source on Windows, `pyreadline3` is installed automatically if the Python interpreter does not provide `readline`.

## Start On Terminal Launch

After installing it, add this block to `~/.bashrc`:

```bash
if [[ $- == *i* ]] && command -v main >/dev/null 2>&1 && [[ -z ${BASH_CHAN_STARTED:-} ]]; then
	export BASH_CHAN_STARTED=1
	main
fi
```

Apply the change to the current shell with:

```bash
source ~/.bashrc
```

## Framework

- `main`: runs commands, stores history, selects reactions, and manages the face process.
- `dialogue_handler.py`: maps existing quotes to `surprised`, `angry`, `annoyed`, `happy`, or `sad` faces.
- `face`: draws the top-right face and handles idle blinking.

Run one command directly with:

```bash
main echo "hello"
```
## Packages

Download the latest platform archive from the [GitHub Releases](https://github.com/spctr-x1/bash-chan-CLI/releases) page:

- Linux: `bash-chan-cli-linux-x86_64.tar.gz`
- Windows: `bash-chan-cli-windows-x86_64.zip`
