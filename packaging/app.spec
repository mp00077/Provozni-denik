from pathlib import Path
import sys

root = Path(SPECPATH).parent
a = Analysis([str(root / "packaging/launcher.py")], pathex=[str(root / "src")],
             binaries=[], datas=[(str(root / "src/provozni_denik/infrastructure/database/migrations"),
                                   "provozni_denik/infrastructure/database/migrations")],
             hiddenimports=["provozni_denik.ui.generated.main_window",
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
          debug=False, strip=False, upx=False, console=False)
collection = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="ProvozniDenik")
if sys.platform == "darwin":
    app = BUNDLE(collection, name="ProvozniDenik.app", bundle_identifier="cz.provoznidenik.desktop")
