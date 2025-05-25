{
  description = "Pipelines run by prefect";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem
    (
      system: let
        pkgs = import nixpkgs {
          inherit system;
        };
        tex = (pkgs.texlive.combine {
          inherit (pkgs.texlive) scheme-small
            anyfontsize
            babel
            babel-latin
            bigfoot
            booktabs
            datetime
            ecclesiastic
            etoolbox
            fmtcount
            fontspec
            gitinfo2
            gregoriotex
            hyperref
            ifthenx
            latexmk
            luacolor
            luamplib
            memoir
            microtype
            paracol
            scalerel
            stackengine
            titlesec
            verse
            xpatch
            xstring
          ;
        });
        buildInputs = with pkgs; [
          (python312.withPackages (ps: [ ps.httpx ]))
          copier
          pre-commit
          tex
          gyre-fonts
        ];
        # allow building c extensions
        env = {
          LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
        };
      in
        with pkgs; {
          devShells.default = mkShell {
            inherit buildInputs;
            inherit env;
          };
        }
    );
}
