class Segment:
    def __init__(self, x1, y1, x2, y2, index):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.a = (y1 - y2)/(x1 - x2)
        self.b = y1 - self.a * x1

        self.index = index


def is_intersection(segment1: Segment, segment2: Segment):   
    if (max(segment1.x1, segment1.x2) < min(segment2.x1, segment2.x2)):
        return False
    
    if (segment1.a == segment2.a):
        return False
    
    Xa = (segment2.b - segment1.b) / (segment1.a - segment2.a)

    if ((Xa < max( min(segment1.x1, segment1.x2), min(segment2.x1, segment2.x2) )) or 
        (Xa > min( max(segment1.x1, segment1.x2), max(segment2.x1, segment2.x2) ))):
        return False 
    else:
        return True
    

def naive_approach(segments):
    result = set()
    for segmenti in segments:
        for segmentj in segments:
            if not is_intersection(segmenti, segmentj):
                continue

            if (segmentj, segmenti) in result:
                continue

            result.add((segmenti, segmentj))

    return result


def tree_approach(segments):
    points = []
    point_map = {}
    
    for segment in segments:
        points.append((segment.x1, segment.y1))
        points.append((segment.x2, segment.y2))

        point_map[(segment.x1, segment.y1)] = segment.index
        point_map[(segment.x2, segment.y2)] = segment.index

    points = sorted(points, key=lambda point: point[0])
    tree = TwoThreeTree()

    for point in points:
        segment = point_map[point[0]]

        if point[0] == segment.x1:
            tree.insert(point[1])

            next_segment_y = tree.getNext(point[1])
            prev_segment_y = tree.getPrev(point[1])
            next_segment = point_map.get(next_segment_y, None)
            prev_segment = point_map.get(prev_segment_y, None)

            if next_segment is not None:
                if is_intersection(segment, next_segment):
                    return segment.index, next_segment.index
                
            if prev_segment is not None:
                if is_intersection(segment, prev_segment):
                    return segment.index, prev_segment.index
        elif point[0] == segment.x2:
            next_segment_y = tree.getNext(point[1])
            prev_segment_y = tree.getPrev(point[1])
            next_segment = point_map.get(next_segment_y, None)
            prev_segment = point_map.get(prev_segment_y, None)

            if next_segment is not None and prev_segment is not None:
                if is_intersection(next_segment, prev_segment):
                    return next_segment.index, prev_segment.index
                
            tree.delete(point[1])
    
    return None


def main():
    pass

if __name__ == '__main__':
    main()