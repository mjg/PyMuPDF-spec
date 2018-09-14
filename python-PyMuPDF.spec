%global pypi_name PyMuPDF
%global desc This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS\
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction\
book formats, and it is known for its top performance and high rendering\
quality.  With PyMuPDF you therefore can also access files with extensions\
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.

Name:           python-%{pypi_name}
Version:        1.13.20
Release:        1%{?dist}
Summary:        Python binding for MuPDF - a lightweight PDF and XPS viewer

# PyMuPDF itself is GPLv3+.  MuPDF (statically linked) is AGPLv3+.
License:        GPLv3+ and AGPLv3+
URL:            https://github.com/rk700/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Can be removed if mupdf provides a shared library
Patch0:         fix-library-linking.patch

BuildRequires:  python2-devel python3-devel
BuildRequires:  gcc
BuildRequires:  zlib-devel mupdf-static
# Can be removed if mupdf provides a shared library
BuildRequires:  libjpeg-devel openjpeg2-devel jbig2dec-devel freetype-devel harfbuzz-devel

%description
%{desc}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%package        doc
Summary:        Documentation for python-%{pypi_name}
BuildArch:      noarch

%description    doc
python-%{pypi_name}-doc contains documentation and examples for PyMuPDF

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install


%files -n python2-%{pypi_name}
%license COPYING "GNU AFFERO GPL V3"
%{python2_sitearch}/fitz/
%{python2_sitearch}/PyMuPDF*

%files -n python3-%{pypi_name}
%license COPYING "GNU AFFERO GPL V3"
%{python3_sitearch}/fitz/
%{python3_sitearch}/PyMuPDF*

%files doc
%doc demo doc/PyMuPDF.pdf examples README.md

%changelog
* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 1.13.20-1
- New upstream release 1.13.20

* Sat Aug 04 2018 Scott Talbert <swt@techie.net> - 1.13.16-1
- New upstream release 1.13.16

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.13.15-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Scott Talbert <swt@techie.net> - 1.13.15-1
- New upstream release 1.13.15

* Fri Jul 20 2018 Scott Talbert <swt@techie.net> - 1.13.14-1
- New upstream release 1.13.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Scott Talbert <swt@techie.net> - 1.13.13-1
- New upstream release 1.13.13

* Wed Jun 27 2018 Scott Talbert <swt@techie.net> - 1.13.12-1
- New upstream release 1.13.12

* Tue Jun 26 2018 Scott Talbert <swt@techie.net> - 1.13.11-1
- New upstream release 1.13.11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.10-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Scott Talbert <swt@techie.net> - 1.13.10-1
- New upstream release 1.13.10

* Sun Jun 10 2018 Scott Talbert <swt@techie.net> - 1.13.9-1
- Initial package.
