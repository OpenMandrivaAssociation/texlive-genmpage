Name:		texlive-genmpage
Version:	15878
Release:	2
Summary:	Generalization of LaTeX's minipages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/genmpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The GenMPage package generalizes LaTeX's minipages. Keyval
options and styles can be used to determine their appearance in
an easy and consistent way. Includes options for paragraph
indentation and vertical alignment with respect to the visual
top and bottom margins.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/genmpage/genmpage.sty
%doc %{_texmfdistdir}/doc/latex/genmpage/README
%doc %{_texmfdistdir}/doc/latex/genmpage/genmpage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/genmpage/genmpage.dtx
%doc %{_texmfdistdir}/source/latex/genmpage/genmpage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
