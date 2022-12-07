_A='v5.3.0'
from typing import List
from localstack.packages import Package,PackageInstaller
from localstack.packages.core import GitHubReleaseInstaller,SystemNotSupportedException
from localstack.utils.platform import get_arch,is_linux,is_mac_os
class K3DPackage(Package):
	def __init__(A):super().__init__('K3D',_A)
	def get_versions(A):return[_A]
	def _get_installer(A,version):return K3DPackageInstaller('k3d',version)
class K3DPackageInstaller(GitHubReleaseInstaller):
	def __init__(A,name,version):super().__init__(name,version,'rancher/k3d')
	def _get_github_asset_name(C):
		A='linux'if is_linux()else'darwin'if is_mac_os()else None;B=get_arch()
		if not A:raise SystemNotSupportedException('Unsupported operating system (currently only Linux/MacOS are supported)')
		return f"k3d-{A}-{B}"
k3d_package=K3DPackage()