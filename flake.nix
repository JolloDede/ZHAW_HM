{
  description = "Pure Python development environment using nixpkgs";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        # Pure Python environment with packages from nixpkgs
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          # Common packages available in nixpkgs
          numpy
          matplotlib
          # requests
          # pandas
          # flask
          # django
          # pytest
          # black
          # flake8
          # mypy
          # rich
          # click
          # pydantic
          # jinja2

          # Add your packages here
          # Note: not all PyPI packages are available in nixpkgs
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv

            # Development tools
            git
          ];

          shellHook = ''
            echo "Pure Nix Python environment activated"
            echo "Python: $(python --version)"
            echo "Available packages are managed purely through Nix"
            echo "To add packages, edit flake.nix and run 'nix flake lock --update-input nixpkgs'"
          '';
        };
      });
}
