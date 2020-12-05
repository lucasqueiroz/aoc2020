use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("day-4/input")?;
    let reader = BufReader::new(file);

    let mut current: String = "".to_string();
    let mut valid = 0;

    for line in reader.lines() {
        let line_str: String = line?;
        if !(line_str.eq("")) {
            current.push_str(&line_str);
        } else {
            if
                current.contains("byr:") &&
                current.contains("iyr:") &&
                current.contains("eyr:") &&
                current.contains("hgt:") &&
                current.contains("hcl:") &&
                current.contains("ecl:") &&
                current.contains("pid:")
            {
                valid = valid + 1;
            }
            current = "".to_string();
        }
    }
    println!("{}", valid);

    Ok(())
}
