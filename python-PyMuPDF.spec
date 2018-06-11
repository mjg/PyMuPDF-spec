%global pypi_name PyMuPDF
%global desc This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS\
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction\
book formats, and it is known for its top performance and high rendering\
quality.  With PyMuPDF you therefore can also access files with extensions\
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.

Name:           python-%{pypi_name}
Version:        1.13.9
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
* Sun Jun 10 2018 Scott Talbert <swt@techie.net> - 1.13.9-1
- Initial package.
