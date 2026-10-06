from pathlib import Path
import sys

root = Path(SPECPATH).parent
sys.path.insert(0, str(root / "scripts"))
from build_metadata import prepare_metadata

metadata = prepare_metadata(root)
exe_options = {}
if sys.platform == "win32":
    exe_options.update(icon=str(metadata["icon"]), version=str(metadata["windows_version"]))
elif sys.platform == "darwin":
    exe_options["icon"] = str(metadata["icon"])
a = Analysis([str(root / "packaging/launcher.py")], pathex=[str(root / "src")],
             binaries=[], datas=[(str(root / "src/provozni_denik/infrastructure/database/migrations"),
                                   "provozni_denik/infrastructure/database/migrations"),
                                  (str(root / "packaging/icons/app.png"), "provozni_denik/ui/resources/icons"),
                                  (str(metadata["metadata"]), "provozni_denik")],
             hiddenimports=["provozni_denik.ui.generated.main_window",
                            "provozni_denik.ui.generated.about_dialog",
                            "provozni_denik.ui.dialogs.about_dialog",
                            "provozni_denik.ui.generated.access_dialog",
                            "provozni_denik.ui.generated.history_view",
                            "provozni_denik.ui.generated.settings_dialog",
                            "provozni_denik.ui.dialogs.access_dialog",
                            "provozni_denik.ui.dialogs.history_dialog",
                            "provozni_denik.ui.dialogs.settings_dialog",
                            "provozni_denik.infrastructure.exports.csv_exporter",
                            "provozni_denik.infrastructure.backups.sqlite_backup"],
             hookspath=[], runtime_hooks=[], excludes=[], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="ProvozniDenik",
          debug=False, strip=False, upx=False, console=False, **exe_options)
collection = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="provozní deník")
if sys.platform == "darwin":
    bundle_options = {}
    info_plist = {"NSHumanReadableCopyright": "Autor: Miroslav Pospíšil"}
    if metadata["version"] is not None:
        numeric_version = ".".join(map(str, metadata["version"].numbers[:3]))
        bundle_options["version"] = numeric_version
        info_plist.update(CFBundleShortVersionString=numeric_version, CFBundleVersion=numeric_version)
    app = BUNDLE(collection, name="provozní deník.app", bundle_identifier="cz.provoznidenik.desktop",
                 icon=str(metadata["icon"]), info_plist=info_plist, **bundle_options)
