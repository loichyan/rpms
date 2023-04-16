%global vtag 20230408-112425-69ae8472
%global debug_package %{nil}

Name:          wezterm
Version:       %(cut -d '-' -f 1 <<< %{vtag})
Release:       %autorelease
Packager:      Loi Chyan <loichyan@foxmail.com>
License:       MIT
URL:           https://wezfurlong.org/%{name}
Summary:       Wez's Terminal Emulator.
Requires:      dbus, fontconfig, openssl, libxcb, libxkbcommon, libxkbcommon-x11, libwayland-client
Requires:      libwayland-egl, libwayland-cursor, mesa-libEGL, xcb-util, xcb-util-keysyms, xcb-util-image, xcb-util-wm
BuildRequires: cargo, make, gcc, gcc-c++
BuildRequires: fontconfig-devel, openssl-devel, libxcb-devel, libxkbcommon-devel, libxkbcommon-x11-devel, wayland-devel
BuildRequires: mesa-libEGL-devel, xcb-util-devel, xcb-util-keysyms-devel, xcb-util-image-devel, xcb-util-wm-devel
Source:        https://github.com/wez/wezterm/releases/download/%{vtag}/%{name}-%{vtag}-src.tar.gz

%description
wezterm is a terminal emulator with support for modern features
such as fonts with ligatures, hyperlinks, tabs and multiple
windows.

%prep
%autosetup -n %{name}-%{vtag}

%build
cargo build --all --release

%install
install -Dm755 assets/open-wezterm-here -t %{buildroot}%{_bindir}
install -Dsm755 target/release/wezterm -t %{buildroot}%{_bindir}
install -Dsm755 target/release/wezterm-mux-server -t %{buildroot}%{_bindir}
install -Dsm755 target/release/wezterm-gui -t %{buildroot}%{_bindir}
install -Dsm755 target/release/strip-ansi-escapes -t %{buildroot}%{_bindir}
install -Dm644 assets/shell-integration/* -t %{buildroot}%{_sysconfdir}/profile.d
install -Dm644 assets/shell-completion/zsh %{buildroot}%{_datadir}/zsh/site-functions/_wezterm
install -Dm644 assets/shell-completion/bash %{buildroot}%{_sysconfdir}/bash_completion.d/wezterm
install -Dm644 assets/icon/terminal.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
install -Dm644 assets/wezterm.desktop %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop
install -Dm644 assets/wezterm.appdata.xml %{buildroot}%{_datadir}/metainfo/org.wezfurlong.wezterm.appdata.xml
install -Dm644 assets/wezterm-nautilus.py %{buildroot}%{_datadir}/nautilus-python/extensions/wezterm-nautilus.py

%files
%{_bindir}/wezterm
%{_bindir}/wezterm-gui
%{_bindir}/wezterm-mux-server
%{_bindir}/strip-ansi-escapes
%{_bindir}/open-wezterm-here
%{_datadir}/zsh/site-functions/_wezterm
%{_sysconfdir}/bash_completion.d/wezterm
%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%{_datadir}/metainfo/org.wezfurlong.wezterm.appdata.xml
%{_datadir}/nautilus-python/extensions/wezterm-nautilus.py*
%{_sysconfdir}/profile.d/*

%changelog
%autochangelog
