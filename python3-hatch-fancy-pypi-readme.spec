# Conditional build:
%bcond_with	tests	# unit tests

%define		module	 hatch-fancy-pypi-readme
Summary:	Fancy PyPI READMEs with Hatch
Summary(pl.UTF-8):	Ozdobne README dla PyPI przy użyciu Hatcha
Name:		python3-%{module}
Version:	24.1.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hatch-fancy-pypi-readme
Source0:	https://files.pythonhosted.org/packages/source/h/hatch-fancy-pypi-readme/hatch_fancy_pypi_readme-%{version}.tar.gz
# Source0-md5:	f5f9e639f066c91f8e623ec6231beae9
URL:		https://pypi.org/project/hatch-fancy-pypi-readme/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
%if %{with tests}
BuildRequires:	python3-pytest
%if "%{_ver_lt %{py3_ver} 3.11}" == "1"
BuildRequires:	python3-tomli
%endif
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-typing_extensions
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
Obsoletes:	python3-hatch_fancy_pypi_readme < 24.1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Your "Fancy" Project Deserves a "Fancy" PyPI Readme!

%description -l pl.UTF-8
"Ozdobny" projekt zasługuje na "ozdobne" readme na PyPI!

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n hatch_fancy_pypi_readme-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG.md LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/hatch-fancy-pypi-readme
%{py3_sitescriptdir}/hatch_fancy_pypi_readme
%{py3_sitescriptdir}/hatch_fancy_pypi_readme-%{version}.dist-info
