# volume_to_miles

Python function to calculate distance walked in a project

## Files

  ### config.json
  This contains the lookup table with the distribution of percentage of people walking as follows:
  |distance (miles)	| percentage of people (fraction) |
  | ------ | ------- |
  | 0.1 | 0.1 |
  | 0.2 | 0.17 |
  | 0.3 | 0.16 |
  | 0.4 | 0.12 |
  | 0.5 | 0.09 |
  | 0.6 | 0.07 |
  | 0.7 | 0.06 |
  | 0.8 | 0.04 |
  | 0.9 | 0.03 |
  | 1.0 | 0.03 |
  | 1.2 | 0.02 |
  | 1.1 | 0.02 |
  | 1.3 | 0.01 |
  | 1.4 | 0.01 |
  | 1.5 | 0.01 |
  | 1.6 | 0.01 |
  | 1.7 | 0.01 |
  | 1.8 | 0.04 |

  ### miles.py
  
  This contains the function that determines the distance walked. 3 parameters are needed as input for the function:
  
  <ol>
    <li> Total path length of the project (proj_distance) </li>
    <li> Total number of intersections within the project boundary (proj_intersections)</li>
    <li> Total intersection volume within the project boundaries (proj_volume) </li>
  </ol>
  
  The function can be called by:
  ```bash
  calculate_distance(proj_distance, proj_intersections, proj_volume)
  ```
  
  It returns a ```float```, the total distance walked within the project for the given intersection volume 

  
## Working

  - Initially, using the project data, the average distance between intersections for the project is calculated. 
  - Using this, the miles travelled by the fraction of people is converted into the number of intersections travelled by the fraction of people. 
  - Using this, the unique number of people in the project for a given volume is calculated. 
  - Once the unique number of people is calculated, using the look-up table above, the total distance travelled by the people in the project is calculated.

## Explanation

1. Calculate the average distance per intersection by dividing total project distance by total number of project intersections.
2. Using the lookup table, and the average distance per intersection from step 1,
find the distribution of percentage of people walking through the number of intersections. (Essentially it's adding another column to the lookup table)

| distance (miles)	| percentage of people (fraction) |
| ----- | ----- |
| .. | .. |

to 

<div class="heatMap">

| distance (miles) | #intersections | percentage of people (fraction) |
| ----- | ----- | ----- |
| .. | .. | .. |
</div>

3. Calculate the total number of intersections people would have travelled according to the updated lookup table. For all rows in the lookup table, iteratively multiply the #intersections with percentage of people (fraction) and sum it up. 
4. Calculate the number of unique people by dividing the total project volume by the total number of intersections travelled (from Step 3).
5. Use the lookup table to multiply the fraction of people with miles travelled by each fraction with the total number of people to get the total distance travelled in the project.
  
