fn main() {
    let array: [u32; 5] = [0;5];
    for index in 0..array.len() + 2 {
        println!("{}: {}", index, array[index])
    }
}
