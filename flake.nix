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
          inherit (pkgs.texlive) scheme-basic
            gregoriotex;
        });
        buildInputs = with pkgs; [
          (python312.withPackages (ps: [ ps.httpx ]))
          copier
          pre-commit
          tex
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
