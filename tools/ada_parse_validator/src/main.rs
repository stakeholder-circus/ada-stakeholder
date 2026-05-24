use std::{env, fs, path::PathBuf};
use tree_sitter::Parser;

fn main() {
    let path = env::args().nth(1).unwrap_or_else(|| "src/stakeholder_registry.ads".to_string());
    let root = PathBuf::from(env::var("CARGO_MANIFEST_DIR").expect("manifest dir"))
        .parent()
        .and_then(|p| p.parent())
        .expect("repo root")
        .to_path_buf();
    let source_path = root.join(path);
    let source = fs::read_to_string(&source_path).expect("read Ada source");
    let mut parser = Parser::new();
    parser.set_language(&tree_sitter_ada::LANGUAGE.into()).expect("load Ada grammar");
    let tree = parser.parse(&source, None).expect("parse Ada source");
    if tree.root_node().has_error() {
        eprintln!("Ada parser found syntax errors in {}", source_path.display());
        std::process::exit(1);
    }
    println!("Ada parser accepted {}", source_path.display());
}
