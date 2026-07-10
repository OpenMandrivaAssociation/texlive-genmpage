%global tl_name genmpage
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.1
Release:	%{tl_revision}.1
Summary:	Generalization of LaTeXs minipages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/genmpage
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genmpage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The GenMPage package generalizes LaTeX's minipages. Keyval options and
styles can be used to determine their appearance in an easy and
consistent way. Includes options for paragraph indentation and vertical
alignment with respect to the visual top and bottom margins.

