Name:		texlive-genmpage
Version:	0.3.1
Release:	1
Summary:	Generalization of LaTeX's minipages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/genmpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The GenMPage package generalizes LaTeX's minipages. Keyval
options and styles can be used to determine their appearance in
an easy and consistent way. Includes options for paragraph
indentation and vertical alignment with respect to the visual
top and bottom margins.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
