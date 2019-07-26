%global pypi_name PyMuPDF
%global desc This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS\
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction\
book formats, and it is known for its top performance and high rendering\
quality.  With PyMuPDF you therefore can also access files with extensions\
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.

Name:           python-%{pypi_name}
Version:        1.14.17
Release:        2%{?dist}
Summary:        Python binding for MuPDF - a lightweight PDF and XPS viewer

# PyMuPDF itself is GPLv3+.  MuPDF (statically linked) is AGPLv3+.
License:        GPLv3+ and AGPLv3+
URL:            https://github.com/rk700/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        https://mupdf.com/downloads/archive/mupdf-1.14.0-source.tar.gz
# Can be removed if mupdf provides a shared library
Patch0:         fix-library-linking.patch
Patch1:         build-mupdf.patch
Patch2:         0001-fix-build-on-big-endian.patch

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  swig
BuildRequires:  zlib-devel
#BuildRequires:  mupdf-static
# Can be removed if mupdf provides a shared library
BuildRequires:  libjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  jbig2dec-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel

%description
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
%autosetup -N -n %{pypi_name}-%{version}
# TEMP build mupdf
%setup -T -D -q -a 1 -n %{pypi_name}-%{version}
%autopatch -p1
cd mupdf-1.14.0-source
for d in $(ls thirdparty | grep -v -e freeglut -e lcms2 -e mujs)
do
  rm -rf thirdparty/$d
done
#%patch0 -p1 -d thirdparty/lcms2
echo > user.make "\
  USE_SYSTEM_FREETYPE := yes
  USE_SYSTEM_HARFBUZZ := yes
  USE_SYSTEM_JBIG2DEC := yes
  USE_SYSTEM_JPEGXR := yes # not used without HAVE_JPEGXR
  USE_SYSTEM_LCMS2 := no # need lcms2-art fork
  USE_SYSTEM_LIBJPEG := yes
  USE_SYSTEM_MUJS := no # build needs source anyways
  USE_SYSTEM_OPENJPEG := yes
  USE_SYSTEM_ZLIB := yes
  USE_SYSTEM_GLUT := no # need freeglut2-art frok
  USE_SYSTEM_CURL := yes
"
cd -

%build
cd mupdf-1.14.0-source
export XCFLAGS="%{optflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK"
make HAVE_X11=no HAVE_GLFW=no HAVE_GLUT=no prefix=$(pwd)/install %{?_smp_mflags}
make HAVE_X11=no HAVE_GLFW=no HAVE_GLUT=no prefix=$(pwd)/install install
unset XCFLAGS
cd -
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} \
  %{__python3} -c 'import sys; sys.path.remove(""); import fitz'


%files -n python3-%{pypi_name}
%license COPYING "GNU AFFERO GPL V3"
%{python3_sitearch}/fitz/
%{python3_sitearch}/PyMuPDF*

%files doc
%doc demo doc/PyMuPDF.pdf examples README.md

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Scott Talbert <swt@techie.net> - 1.14.17-1
- Update to new upstream release 1.14.17 (#1727474)

* Thu Jun 13 2019 Scott Talbert <swt@techie.net> - 1.14.16-1
- Update to new upstream release 1.14.16 (#1713110)

* Wed Jun 12 2019 Scott Talbert <swt@techie.net> - 1.14.14-3
- Temporarily build our own copy of mupdf to fix FTBFS (#1716518)

* Tue May 07 2019 Scott Talbert <swt@techie.net> - 1.14.14-2
- Restore linking with harfbuzz (#1706753)

* Thu Apr 18 2019 Scott Talbert <swt@techie.net> - 1.14.14-1
- New upstream release 1.14.14

* Mon Apr 08 2019 Scott Talbert <swt@techie.net> - 1.14.13-1
- New upstream release 1.14.13

* Fri Mar 22 2019 Scott Talbert <swt@techie.net> - 1.14.12-1
- New upstream release 1.14.12

* Tue Mar 12 2019 Scott Talbert <swt@techie.net> - 1.14.10-1
- New upstream release 1.14.10

* Fri Mar 08 2019 Scott Talbert <swt@techie.net> - 1.14.9-1
- New upstream release 1.14.9

* Thu Jan 31 2019 Scott Talbert <swt@techie.net> - 1.14.8-1
- New upstream release 1.14.8

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 1.14.7-1
- New upstream release 1.14.7

* Tue Nov 20 2018 Scott Talbert <swt@techie.net> - 1.14.1-1
- New upstream release 1.14.1

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.20-2
- Subpackage python2-PyMuPDF has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

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
