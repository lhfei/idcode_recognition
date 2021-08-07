"""

"""

class IDCodeFormater(object):
    def format(self, res, target_str):
        target_array = target_str.replace('"', '').split()
        res =  self.get_target(res, target_array)
        for item in res:
            crop = item['crop']
            item['coordinate'] = [(crop[0]+crop[2])/2, (crop[1]+crop[3])/2]

        result = self.wrap_result(res, target_array)
        return result

    """
    @res 
    @target 
    """
    def get_target(self, res, target_array):
        result = []
        for target in target_array:
            plain = [x for x in res if x['content'] == target]
            if len(plain) == 1:
                result.append(plain[0])
        return result;

    def wrap_result(self, res, target_array):
        return {
            "result": len(res) == len(target_array),
            "recognition": res
        }