func CountSheeps(numbers []bool) int {
	longitud := len(numbers)
	var count int
	for i := 0; i < longitud; i++ {
	  if numbers[i] == true {
		count++
	  }
	}
	return count 
  }