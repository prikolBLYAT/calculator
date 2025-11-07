[Setup]
AppName=Calculator
AppVersion=1.0
AppPublisher=ВашаКоманда
DefaultDirName={pf}\Calculator
DefaultGroupName=Calculator
OutputBaseFilename=Calculator_Installer_v1.0
Compression=lzma
SolidCompression=yes
LicenseFile=installer_files\LICENSE.txt

[Languages]
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"

[Files]
Source: "installer_files\Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer_files\LICENSE.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
Name: "{group}\Calculator"; Filename: "{app}\Calculator.exe"
Name: "{commondesktop}\Calculator"; Filename: "{app}\Calculator.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе"; GroupDescription: "Дополнительно:"; Flags: unchecked

[Run]
Filename: "{app}\Calculator.exe"; Description: "Запустить Calculator"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
