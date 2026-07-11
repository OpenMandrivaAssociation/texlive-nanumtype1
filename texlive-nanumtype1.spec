%global tl_name nanumtype1
%global tl_revision 29558

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Type1 subfonts of Nanum Korean fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/nanumtype1
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nanumtype1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nanumtype1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Nanum is a unicode font designed especially for Korean-language script.
The font was designed by Sandoll Communication and Fontrix; it includes
the sans serif (gothic), serif (myeongjo), pen script and brush script
typefaces. The package provides Type1 subfonts converted from Nanum
Myeongjo (Regular and ExtraBold) and Nanum Gothic (Regular and Bold)
OTFs. C70, LUC, T1, and TS1 font definition files are also provided.
(The package does not include OpenType/TrueType files, which are
available from Naver)

