Split-SSH
=========

A Salt state that enables [split-SSH][split-ssh] in Qubes OS.

Overview
--------

- Ensures the existence of a `ssh-vault` qube that starts automatically on system startup. This qube has no network access and holds SSH keys.
- Ensures the presence of a Qubes RPC policy in `dom0`. That policy ensures that the user is asked before any qube accesses the SSH keys contained in `ssh-vault`.
- Ensures a `ssh-client` qube exists. That qube is configured to allow usage of SSH but relies on the SSH keys contained in `ssh-vault`.

Installation
------------

Copy, or type the contents of this repository into `/srv/salt/split-ssh/` (inspect the surounding files and apply similar permissions and ownership to the `srv/salt/split-ssh` directory).

Alternatively, you can build and sign an RPM package in order to install it in _dom0_. See [qubes-mgmt-salt-user-split-ssh][rpm].

  [rpm]: https://github.com/gonzalo-bulnes/qubes-mgmt-salt-user/tree/main/states/split-ssh

Usage
-----

Enable the top files:

```sh
sudo qubesctl top.enable split-ssh.client split-ssh.policy split-ssh.vault
```

Apply the state:

```sh
sudo qubesctl --targets=fedora-32,ssh-client,ssh-vault state.apply
```

**Note**: the `ssh-client` and `ssh-vault` machines will be created if they don't exist. That is the point of having a Salt state! They are part of the targets because because part of the configuration applies to them.

Once the state is enforced, create new SSH keys in `ssh-vault` (or copy existing keys if you prefer).

References
----------

- [Using split ssh in QubesOS 4.0][split-ssh]

  [split-ssh]: https://kushaldas.in/posts/using-split-ssh-in-qubesos-4-0.html