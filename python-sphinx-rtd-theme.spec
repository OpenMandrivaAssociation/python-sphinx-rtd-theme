%define module sphinx_rtd_theme

Summary:	Sphinx theme for use with Read the Docs
Name:		python-%{module}
Version:	1.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-rtd-theme/sphinx_rtd_theme-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/sphinx-rtd-theme/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description
This Sphinx theme was designed to provide a great reader experience for
documentation users on both desktop and mobile devices. This theme is used
primarily on Read the Docs but can work with any Sphinx project.

You can find a working demo of the theme in the theme documentation

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/sphinx_rtd_theme-%{version}-py*.*.egg-info/PKG-INFO
%{python_sitelib}/sphinx_rtd_theme-%{version}-py*.*.egg-info
%{python_sitelib}/sphinx_rtd_theme/
