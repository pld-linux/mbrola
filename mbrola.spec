# NOTE:
# - x86_64 version is actually 3.01d
Summary:	MBROLA - a speech synthesizer based on the concatenation of diphones
Summary(pl.UTF-8):	MBROLA - syntezator mowy bazujący na łączeniu dwuzgłosek
Name:		mbrola
Version:	301h
Release:	7
License:	Non-commercial, non-military purposes, w/ and only w/ the voice and language databases available on http://tcts.fpms.ac.be/synthesis/
Group:		Applications/Sound
Source0:	http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr%{version}.zip
# Source0-md5:	95314c9a545918729a5965f86859a28e
Source1:	http://tcts.fpms.ac.be/synthesis/%{name}/bin/amd64linux/mbrola.zip
# Source1-md5:	49e95e232d8d996351ad04dcc6392857
URL:		http://tcts.fpms.ac.be/synthesis/mbrola.html
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664} ppc alpha sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MBROLA is a speech synthesizer based on the concatenation of diphones.
It takes a list of phonemes as input, together with prosodic
information (duration of phonemes and a piecewise linear description
of pitch), and produces speech samples on 16 bits (linear), at the
sampling frequency of the diphone database.

It is therefore NOT a Text-To-Speech (TTS) synthesizer, since it does
not accept raw text as input. In order to obtain a full TTS system,
you need to use this synthesizer in combination with a text processing
system that produces phonetic and prosodic commands.

%description -l pl.UTF-8
MBROLA jest syntezatorem mowy opartym o połączenia dwuzgłosek. Jako
dane wejściowe pobiera listę fonemów, łącznie z informacją prozodyczną
(długość fonemów oraz cząstkowy liniowy opis tonacji), po czym tworzy
16-bitowe (liniowe) próbki mowy o częstotliwości próbkowania pobranej
z bazy dwuzgłosek.

NIE jest to syntezator przetwarzający tekst na mowę (Text-To-Speech,
TTS), gdyż nie przyjmuje jako danych wejściowych czystego tekstu. Aby
uzyskać pełny system TTS trzeba posługiwać się tym syntezatorem
łącznie z systemem przetwarzania tekstu, który tworzy polecenia
fonetyczno-prozodyczne jako dane wynikowe.

%prep
%setup -q -c -T -a 0 -a 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%ifarch %{ix86}
install -p mbrola-linux-i386 $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch x86_64
install -p mbrola $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch ppc
install -p mbrola206a-linux-ppc $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch alpha
install -p mbrola-linux-alpha $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch sparc
install -p mbrola-SuSElinux-ultra1.dat $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/mbrola

%define date	%(LC_ALL="C" date +"%a %b %d %Y")
%changelog
* %{date}  PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: mbrola.spec,v $
Revision 1.25  2009-10-22 19:15:52  glen
- preserve perms; rel 7

Revision 1.24  2009/06/06 11:50:03  glen
- use macro for x86_64 arches; rel 6

Revision 1.23  2009/06/06 08:17:50  cactus
- add arch x86_64

Revision 1.22  2008/03/13 21:21:20  glen
- sparc already handled

Revision 1.21  2008-03-02 23:48:17  glen
- sound datafiles moved to mbrola-voices.spec; rel 5

Revision 1.20  2007-03-03 12:14:34  arekm
- rel 4

Revision 1.19  2007/02/13 06:46:53  glen
- tabs in preamble

Revision 1.18  2007/02/12 00:49:07  baggins
- converted to UTF-8

Revision 1.17  2005/05/26 20:16:00  ankry
- fixed %doc

Revision 1.16  2005/02/26 20:06:01  darekr
- BR: unzip

Revision 1.15  2004/10/06 23:10:34  havner
- rel 3

Revision 1.14  2004/06/19 17:58:02  qboosh
- sorted subpackages, some desc fixes
- some docs probably need fix, files were silently overwritten previously

Revision 1.13  2004/06/15 11:39:42  djurban
- finished, added sparc binary, ppc binary is now version 302 instead od 206 earlier

Revision 1.12  2004/06/15 11:19:15  djurban
- added files for nie pkgs

Revision 1.11  2004/06/15 11:12:08  djurban
- nearly finished %prep works, %install needs a oneliner. commiting to add %files on a different machine

Revision 1.10  2004/06/13 17:13:03  djurban
- begin update, added 60 voices for different language (incl. german, french, hebrew, italian etc.)

Revision 1.9  2004/04/26 17:05:05  adamg
- release 2 for Ac (1 is for Ra)

Revision 1.8  2003/05/28 12:59:42  malekith
- massive attack: source-md5

Revision 1.7  2003/05/25 05:50:29  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.6  2002/08/06 11:05:06  wolf
- added r: %{name} to subpackages

Revision 1.5  2002/08/06 01:25:03  wolf
- finished, STBR

Revision 1.4  2002/08/06 01:00:25  wolf
- works, but still not finished

Revision 1.3  2002/08/05 20:38:03  ankry
- pl description
- adapterized

Revision 1.2  2002/08/04 17:25:09  ankry
- fixed package names

Revision 1.1  2002/08/02 21:47:57  hunter
- NYF
