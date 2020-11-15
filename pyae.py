from decimal import Decimal # Used to offer any user-defined precision.

class ArithmeticEncoding:
    """
    ArithmeticEncoding is a class for building the arithmetic encoding.
    """

    def __init__(self, frequency_table, save_stages=False):
        """
        frequency_table: Frequency table as a dictionary where key is the symbol and value is the frequency.
        save_stages: If True, then the intervals of each stage are saved in a list. Note that setting save_stages=True may cause memory overflow if the message is large
        """
        
        self.save_stages = save_stages
        if(save_stages == True):
            print("WARNING: Setting save_stages=True may cause memory overflow if the message is large.")

        self.probability_table = self.get_probability_table(frequency_table)

    def get_probability_table(self, frequency_table):
        """
        Calculates the probability table out of the frequency table.
        """
        total_frequency = sum(list(frequency_table.values()))

        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value/total_frequency

        return probability_table

    def get_encoded_value(self, last_stage_probs):
        """
        After encoding the entire message, this method returns the single value that represents the entire message.
        """
        last_stage_probs = list(last_stage_probs.values())
        last_stage_values = []
        for sublist in last_stage_probs:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)

        return (last_stage_min + last_stage_max)/2

    def process_stage(self, probability_table, stage_min, stage_max):
        """
        Processing a stage in the encoding/decoding process.
        """
        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = Decimal(probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    def encode(self, msg, probability_table):
        """
        Encodes a message.
        """
        
        # Make sure 
        msg = list(msg)

        encoder = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)

            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            if self.save_stages:
                encoder.append(stage_probs)

        last_stage_probs = self.process_stage(probability_table, stage_min, stage_max)
        
        if self.save_stages:
            encoder.append(last_stage_probs)

        encoded_msg = self.get_encoded_value(last_stage_probs)

        return encoded_msg, encoder

    def decode(self, encoded_msg, msg_length, probability_table):
        """
        Decodes a message.
        """

        decoder = []

        decoded_msg = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for idx in range(msg_length):
            stage_probs = self.process_stage(probability_table, stage_min, stage_max)

            for msg_term, value in stage_probs.items():
                if encoded_msg >= value[0] and encoded_msg <= value[1]:
                    break

            decoded_msg.append(msg_term)

            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            if self.save_stages:
                decoder.append(stage_probs)

        if self.save_stages:
            last_stage_probs = self.process_stage(probability_table, stage_min, stage_max)
            decoder.append(last_stage_probs)

        return decoded_msg, decoder
