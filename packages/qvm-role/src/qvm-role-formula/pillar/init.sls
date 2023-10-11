qvm-role:
  debian-12-minimal:
    template_installed:
      - fromrepo: qubes-templates-itl
  
  debian-12-minimal-srv:
    clone:
      - source: debian-12-minimal
    features:
      - set:
          - pillar.nfs.server.enable: True
  
  debian-12-minimal-home:
    clone:
      - source: debian-12-minimal
    features:
      - set:
          - pillar.nfs.client.enable: True
  
  #bcd-files:
  #  qvm.present:
  #  qvm.prefs:
  #    label: blue
  #    template: debian-12-minimal-srv    
  #  qvm.features:
  #    - enable:
  #        - pillar.nfs.server.export.Documents.hosts.workstation.options: [rw]
  #        - pillar.nfs.server.export.Documents.hosts.backup.options: [ro]
  #        - supported-service.nfs: True
  
  #debian-12-minimal-home:
  #  type:
  #    template.clone
  #    	source: debian-12-minimal
  #  features:
  #    pillar.nfs.client.enable: True
  #  prefs:
  #    label: black
  #bcd-files:
  #  type:
  #    app:
  #  prefs:
  #    label: blue
  #    template: debian-12-minimal-srv
  #  features:
  #    pillar.nfs.server.export.Documents.hosts.workstation.options: [rw]
  #    pillar.nfs.server.export.Documents.hosts.backup.options: [ro]
  #    supported-service.nfs: True
  #bcd-home-dvm:
  #  type:
  #    app:
  #  prefs:
  #    label: black
  #    template_for_dispvms: True
  #  features:
  #    pillar.nfs.client.mount.home-user-Documents.What.client: workstation
  #    pillar.nfs.client.mount.home-user-Documents.What.server: bcd-files
  #    pillar.nfs.client.mount.home-user-Documents.What.export: /Documents
  #bcd-home: 
  #  type: 
  #    disp:
  #  prefs:
  #    label: blue
  #    template: bcd-home-dvm
  #  features:
  #    supported-service.connectnfs-mount: True
  #bcd-backup-dvm:
  #  type:
  #    disp:
  #  prefs:
  #    label: black
  #    template_for_dispvms: True
  #  features:
  #    pillar.nfs.client.mount.mnt-Documents.What: backup@bcd-files:/Documents
  #bcd-backup:
  #  type:
  #    app:
  #  prefs:
  #    label: blue
  #    template: bcd-backup-dvm
  #  features:
  #    supported-service.connectnfs-mount: True
