# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/genmpage
# catalog-date 2007-03-07 00:33:49 +0100
# catalog-license lppl
# catalog-version 0.3.1
Name:		texlive-genmpage
Version:	0.3.1
Release:	12
Summary:	Generalization of LaTeX's minipages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/genmpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3.1-2
+ Revision: 752241
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3.1-1
+ Revision: 718532
- texlive-genmpage
- texlive-genmpage
- texlive-genmpage
- texlive-genmpage

